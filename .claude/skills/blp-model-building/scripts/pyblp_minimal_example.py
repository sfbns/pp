"""最小可运行 pyblp 示例（pyblp 1.2.0 自带的 Nevo 麦片数据），把 skill 的"估计"一节落到代码上。

运行（本机已建好装有 pyblp 1.2.0 与 pandas 的虚拟环境，不碰全局 Python）：
    D:\\blp-structural-skill-config\\work_20261007\\venv_pyblp\\Scripts\\python.exe pyblp_minimal_example.py
加 --show-bound-trap 会再用 L-BFGS-B 跑一遍，演示默认下界 σ ≥ 0 怎样卡住一个参数（多约 2 分钟）。
该 bounded 运行仅是演示，不作为已接受估计。其实际失败/边界状态独立报告。
负向验收：加 --force-stage-failure optimal-IV（或 main、micro），真实把该阶段 maxiter 设为 0；必须 exit 1。

做六件事：
  1. 随机系数 logit + 人口特征交互（Nevo 规格：价格进 X1，产品固定效应吸收，X2 含常数、价格、糖分、口感）；
  2. 收敛诊断：投影梯度范数、约化 Hessian 特征值（全为正才是局部极小），以及 σ 的对角元；
  3. 估计后对象：弹性、加价（勒纳指数）、边际成本、转移率、消费者剩余；
  4. 用近似最优工具（Chamberlain）重估；
  5. 微观矩的接口写法：目标值取同一模型的拟合值，只演示 MicroDataset / MicroPart / MicroMoment 怎么写，不代表真实调查；
  6. 打印一致性检查：收敛与诊断通过、价格自导数为负、交叉导数非负（Nevo 数据没有网络效应）、加价为正。

优化器用不带边界的 BFGS（pyblp 教程对 Nevo 的设定）。不要换成 L-BFGS-B 而不设 sigma_bounds：
支持边界的优化器下 pyblp 默认把 σ 的对角元限制为非负；Nevo 每个市场只有 20 个固定且不对称的抽样，
g(σ) ≠ g(−σ)，于是糖分的 σ 会被卡在 0（目标函数 4.72 对无约束的 4.56），见 --show-bound-trap。
内层收缩用 SQUAREM、容差 1E-14（Conlon & Gortmaker 2020 的建议，见 references/estimation_algorithm_and_code.md §0.3）。
"""
import argparse
import json
import sys
import traceback

import numpy as np
import pandas as pd
import pyblp

if hasattr(sys.stdout, "reconfigure"):                    # Windows GBK consoles cannot print Greek letters
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

pyblp.options.verbose = False
pyblp.options.digits = 4

# These scientific acceptance tolerances are declared once, before estimation.
# Optimizer termination is necessary, but does not replace score / curvature checks.
PROJECTED_GRADIENT_TOL = 1e-4
HESSIAN_MIN_EIGENVALUE = 1e-8
OPTIMIZER_GTOL = 1e-5
REQUIRED_STAGES = ("main", "optimal-IV", "micro")
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--show-bound-trap", action="store_true")
parser.add_argument("--force-stage-failure", choices=REQUIRED_STAGES,
                    help="negative test: use a zero-iteration optimizer for one required stage")
args = parser.parse_args()
stage_records = {}
demonstration_records = {}
post_checks = {"completed": False}
post_errors = []


def unavailable_stage(label, error, required=True):
    """Record a real exception / unmet dependency; never turn it into a passing stage."""
    record = {"stage": label, "required": required, "executed": bool(error.get("attempted_solve", False)),
              "converged": False, "projected_gradient_norm": None,
              "hessian_eigenvalue_min": None, "hessian_eigenvalue_max": None,
              "finite_checks": {}, "inner_fixed_points_converged": None,
              "errors": [error], "scientific_gate_pass": False, "accepted": False,
              "classification": "required_failed" if required else "demonstration_failed_not_accepted"}
    (stage_records if required else demonstration_records)[label] = record
    print("STAGE_DIAGNOSTICS " + json.dumps(record, ensure_ascii=False, allow_nan=False))


def diagnostics(res, label, required=True):
    """Record the actual state and gate every required re-estimation, not only main."""
    finite_checks = {}
    for name in ("objective", "sigma", "pi", "beta", "delta", "xi", "gradient",
                 "projected_gradient", "projected_gradient_norm", "reduced_hessian",
                 "reduced_hessian_eigenvalues", "W"):
        try:
            finite_checks[name] = bool(np.isfinite(np.asarray(getattr(res, name), dtype=float)).all())
        except (AttributeError, TypeError, ValueError):
            finite_checks[name] = False
    raw_pgn = np.asarray(res.projected_gradient_norm, dtype=float)
    pgn = float(raw_pgn.item()) if raw_pgn.size == 1 and np.isfinite(raw_pgn).all() else None
    eig = np.asarray(res.reduced_hessian_eigenvalues, dtype=float).ravel()
    finite_eig = eig.size > 0 and bool(np.isfinite(eig).all())
    eig_min = float(eig.min()) if finite_eig else None
    eig_max = float(eig.max()) if finite_eig else None
    # pyblp 1.2.0 stores final computational errors here. Unknown API is not an empty error list.
    raw_errors = getattr(res, "_errors", None)
    errors = ([{"type": type(error).__name__, "message": str(error)} for error in raw_errors]
              if raw_errors is not None else
              [{"type": "UnsupportedDiagnosticsAPI", "message": "ProblemResults._errors unavailable"}])
    fp = np.asarray(res.fp_converged, dtype=bool)
    inner_ok = bool(fp.size and fp.all())
    checks = {"converged": bool(res.converged),
              "cumulative_converged": bool(res.cumulative_converged),
              "projected_gradient": pgn is not None and pgn <= PROJECTED_GRADIENT_TOL,
              "positive_reduced_hessian": eig_min is not None and eig_min > HESSIAN_MIN_EIGENVALUE,
              "finite_numbers": all(finite_checks.values()),
              "inner_fixed_points": inner_ok, "no_computational_errors": not errors}
    scientific_pass = all(checks.values())
    record = {"stage": label, "required": required, "executed": True,
              "objective": float(np.asarray(res.objective).item()) if finite_checks["objective"] else None,
              "converged": bool(res.converged), "cumulative_converged": bool(res.cumulative_converged),
              "projected_gradient_norm": pgn,
              "projected_gradient_tolerance": PROJECTED_GRADIENT_TOL,
              "hessian_eigenvalue_min": eig_min, "hessian_eigenvalue_max": eig_max,
              "hessian_min_required": HESSIAN_MIN_EIGENVALUE,
              "hessian_eigenvalues": eig.tolist() if finite_eig else [],
              "finite_checks": finite_checks, "inner_fixed_points_converged": inner_ok,
              "errors": errors, "checks": checks, "scientific_gate_pass": scientific_pass,
              "accepted": bool(required and scientific_pass),
              "classification": ("required_accepted" if scientific_pass else "required_failed")
              if required else "demonstration_only_not_accepted"}
    (stage_records if required else demonstration_records)[label] = record
    print("STAGE_DIAGNOSTICS " + json.dumps(record, ensure_ascii=False, allow_nan=False))
    print(f"[{label}] diag(sigma) =", np.round(np.diag(res.sigma), 4))
    return record


def solve_stage(label, stage_problem, sigma, pi, iteration, **kwargs):
    options = {"gtol": OPTIMIZER_GTOL}
    if args.force_stage_failure == label:
        options["maxiter"] = 0     # actual optimizer failure, not a mocked result or edited score
    try:
        result = stage_problem.solve(sigma, pi, optimization=pyblp.Optimization("bfgs", options),
                                     iteration=iteration, method="1s", error_behavior="raise", **kwargs)
        diagnostics(result, label)
        return result
    except Exception as error:
        unavailable_stage(label, {"type": type(error).__name__, "message": str(error),
                                  "traceback": traceback.format_exc(), "attempted_solve": True})
        return None


def finish():
    accepted = all(stage_records.get(label, {}).get("accepted", False) for label in REQUIRED_STAGES)
    ok = bool(accepted and all(post_checks.values()) and not post_errors)
    summary = {"required_stages": stage_records, "demonstrations": demonstration_records,
               "post_estimation_checks": post_checks, "post_estimation_errors": post_errors,
               "versions": {"python": sys.version.split()[0], "pyblp": pyblp.__version__,
                            "numpy": np.__version__, "pandas": pd.__version__},
               "forced_stage_failure": args.force_stage_failure,
               "required_stage_acceptance": accepted, "ok": ok,
               "bounded_demo_is_accepted": False,
               "bounded_demo_affects_required_acceptance": False}
    print("FINAL_DIAGNOSTICS " + json.dumps(summary, ensure_ascii=False, allow_nan=False))
    print("REQUIRED CHECKS PASS (main + optimal-IV + micro; demonstrations excluded)" if ok
          else "REQUIRED CHECKS FAILED")
    sys.exit(0 if ok else 1)

product_data = pd.read_csv(pyblp.data.NEVO_PRODUCTS_LOCATION)
agent_data = pd.read_csv(pyblp.data.NEVO_AGENTS_LOCATION)

# ---- 1. specification: X1 (linear, product FE absorbed), X2 (random coefficients), demographics
X1 = pyblp.Formulation("0 + prices", absorb="C(product_ids)")
X2 = pyblp.Formulation("1 + prices + sugar + mushy")
demographics = pyblp.Formulation("0 + income + income_squared + age + child")
problem = pyblp.Problem((X1, X2), product_data, demographics, agent_data)

# zeros in pi are fixed at zero; nonzeros are free starting values (rows = X2 terms, cols = demographics)
sigma0 = np.diag([0.33, 2.45, 0.016, 0.24])
pi0 = np.array([
    [5.48, 0.0, 0.20, 0.0],
    [15.9, -1.2, 0.0, 2.63],
    [-0.25, 0.0, 0.05, 0.0],
    [1.27, 0.0, -0.81, 0.0],
])
iteration = pyblp.Iteration("squarem", {"atol": 1e-14})
print("== RC logit (Nevo spec, unbounded BFGS) ==")
results = solve_stage("main", problem, sigma0, pi0, iteration)
if results is None:
    for label in ("optimal-IV", "micro"):
        unavailable_stage(label, {"type": "DependencyFailed", "message": "main result unavailable"})
    finish()
print("price coefficient (beta, linear part):", np.round(results.beta.ravel(), 3))

# ---- 3. post-estimation objects (per market, stacked)
try:
    elasticities = results.compute_elasticities()          # J_t x J_t blocks stacked by market
    markups = results.compute_markups()                    # Lerner index (p − c)/p under multi-product Bertrand
    costs = results.compute_costs()
    diversion = results.compute_diversion_ratios()
    cs = results.compute_consumer_surpluses()
    t0 = product_data["market_ids"].iloc[0]
    rows = (product_data["market_ids"] == t0).to_numpy()
    E0 = elasticities[rows][:, : rows.sum()]
    J0 = results.compute_demand_jacobians(market_id=t0)   # transpose before building BLP's Δ by hand
    off = ~np.eye(J0.shape[0], dtype=bool)
    post_checks = {"completed": True, "own_derivatives_first_market": bool((np.diag(J0) < 0).all()),
                   "cross_derivatives_first_market": bool((J0[off] >= -1e-12).all()),
                   "positive_lerner_all_products": bool((markups > 0).all())}
    post_checks.update({"finite_" + name: bool(np.isfinite(array).all()) for name, array in
                        (("elasticities", elasticities), ("markups", markups), ("costs", costs),
                         ("diversion", diversion), ("surpluses", cs), ("jacobian_first_market", J0))})
    print("POST_DIAGNOSTICS " + json.dumps(post_checks, allow_nan=False))
    print("market", t0, ": mean own elasticity", round(float(np.diag(E0).mean()), 3),
          "| mean Lerner (p−c)/p", round(float(markups.mean()), 4))
    print("mean consumer surplus across markets:", round(float(np.mean(cs)), 4))
except Exception as error:
    post_errors.append({"type": type(error).__name__, "message": str(error),
                        "traceback": traceback.format_exc()})

# ---- 4. approximate optimal instruments, then re-estimate
print("== with approximate optimal instruments ==")
try:
    instrument_results = results.compute_optimal_instruments(method="approximate")
    if not np.isfinite(instrument_results.demand_instruments).all():
        raise ValueError("approximate optimal demand instruments contain nonfinite values")
    updated_problem = instrument_results.to_problem()
    updated = solve_stage("optimal-IV", updated_problem, results.sigma, results.pi, iteration)
    if updated is not None:
        print("price coefficient:", np.round(updated.beta.ravel(), 3))
except Exception as error:
    unavailable_stage("optimal-IV", {"type": type(error).__name__, "message": str(error),
                                     "traceback": traceback.format_exc(), "preparation_failed": True})

# ---- 5. micro-moment interface: E[income | inside purchase] among a survey of inside purchasers
inside_buyers = pyblp.MicroDataset(
    name="inside purchasers (illustrative)",
    observations=2000,
    compute_weights=lambda t, p, a: np.c_[np.zeros((a.size, 1)), np.ones((a.size, p.size))],
)
income_part = pyblp.MicroPart(
    name="income among inside purchasers",
    dataset=inside_buyers,
    compute_values=lambda t, p, a: np.c_[np.zeros((a.size, 1)), np.outer(a.demographics[:, 0], np.ones(p.size))],
)
placeholder = pyblp.MicroMoment(name="E[income | inside]", value=0.0, parts=income_part)
print("== with one micro moment (target = model-implied value, interface demo only) ==")
try:
    model_value = float(np.asarray(results.compute_micro_values([placeholder])).ravel()[0])
    if not np.isfinite(model_value):
        raise ValueError("illustrative micro target is nonfinite")
    micro_moment = pyblp.MicroMoment(name="E[income | inside]", value=model_value, parts=income_part)
    micro_results = solve_stage("micro", problem, results.sigma, results.pi, iteration,
                                micro_moments=[micro_moment])
    if micro_results is not None:
        print("target", round(model_value, 4), "| re-estimated price coefficient", np.round(micro_results.beta.ravel(), 3))
except Exception as error:
    unavailable_stage("micro", {"type": type(error).__name__, "message": str(error),
                                "traceback": traceback.format_exc(), "preparation_failed": True})

# ---- optional: the bound trap
if args.show_bound_trap:
    print("== same problem with L-BFGS-B and pyblp's default bound diag(sigma) >= 0 ==")
    try:
        bounded = problem.solve(sigma0, pi0, optimization=pyblp.Optimization("l-bfgs-b", {"gtol": 1e-6}),
                                iteration=iteration, method="1s", error_behavior="raise")
        diagnostics(bounded, "bounded", required=False)
        at_bound = np.isclose(np.diag(bounded.sigma), 0.0, atol=1e-10) & ~np.isclose(np.diag(sigma0), 0.0)
        stuck = [n for n, b in zip(["1", "prices", "sugar", "mushy"], at_bound) if b]
        demonstration_records["bounded"]["sigma_at_lower_bound"] = stuck
        print("BOUND_DEMONSTRATION_NOT_ACCEPTED; sigma diagonal elements at lower bound 0:", stuck)
    except Exception as error:
        unavailable_stage("bounded", {"type": type(error).__name__, "message": str(error),
                                      "traceback": traceback.format_exc(), "attempted_solve": True}, required=False)

finish()
