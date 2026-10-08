"""最小可运行 pyblp 示例（pyblp 1.2.0 自带的 Nevo 麦片数据），把 skill 的"估计"一节落到代码上。

运行（本机已建好装有 pyblp 1.2.0 与 pandas 的虚拟环境，不碰全局 Python）：
    D:\\blp-structural-skill-config\\work_20261007\\venv_pyblp\\Scripts\\python.exe C:\\Users\\于舒奕\\.claude\\skills\\blp-model-building\\scripts\\pyblp_minimal_example.py
加 --show-bound-trap 会再用 L-BFGS-B 跑一遍，演示默认下界 σ ≥ 0 怎样卡住一个参数（多约 2 分钟）。

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
import sys

import numpy as np
import pandas as pd
import pyblp

if hasattr(sys.stdout, "reconfigure"):                    # Windows GBK consoles cannot print Greek letters
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

pyblp.options.verbose = False
pyblp.options.digits = 4

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
optimization = pyblp.Optimization("bfgs", {"gtol": 1e-5})   # unbounded; bounds would be ignored anyway
iteration = pyblp.Iteration("squarem", {"atol": 1e-14})
results = problem.solve(sigma0, pi0, optimization=optimization, iteration=iteration, method="1s")


def diagnostics(res, label):
    """Print and return (projected gradient norm, min reduced-Hessian eigenvalue)."""
    pgn = float(np.max(np.abs(np.asarray(res.projected_gradient_norm, dtype=float))))
    eig = np.asarray(res.reduced_hessian_eigenvalues, dtype=float).ravel()
    print(f"[{label}] objective {float(res.objective):.4f} | converged {res.converged} | "
          f"projected gradient norm {pgn:.1e} | reduced-Hessian eigenvalues min {eig.min():.2e}, max {eig.max():.2e}")
    print(f"[{label}] diag(sigma) =", np.round(np.diag(res.sigma), 4))
    return pgn, float(eig.min())


print("== RC logit (Nevo spec, unbounded BFGS) ==")
print("price coefficient (beta, linear part):", np.round(results.beta.ravel(), 3))
pgn, eig_min = diagnostics(results, "main")
diag_ok = bool(results.converged) and pgn < 1e-4 and eig_min > 0

# ---- 3. post-estimation objects (per market, stacked)
elasticities = results.compute_elasticities()          # J_t x J_t blocks stacked by market
markups = results.compute_markups()                    # Lerner index (p − c)/p under multi-product Bertrand (firm_ids)
costs = results.compute_costs()
diversion = results.compute_diversion_ratios()
cs = results.compute_consumer_surpluses()
t0 = product_data["market_ids"].iloc[0]
rows = (product_data["market_ids"] == t0).to_numpy()
E0 = elasticities[rows][:, : rows.sum()]
J0 = results.compute_demand_jacobians(market_id=t0)   # (j,k) = ∂s_j/∂p_k; transpose before building BLP's Δ by hand
own_ok = bool((np.diag(J0) < 0).all())
off = ~np.eye(J0.shape[0], dtype=bool)
cross_ok = bool((J0[off] >= -1e-12).all())             # valid here: Nevo cereal demand has no network terms
print("market", t0, ": mean own elasticity", round(float(np.diag(E0).mean()), 3),
      "| own ∂s/∂p < 0:", own_ok, "| cross ∂s/∂p ≥ 0:", cross_ok,
      "| Lerner > 0:", bool((markups > 0).all()), "| mean Lerner (p−c)/p", round(float(markups.mean()), 4))
print("mean consumer surplus across markets:", round(float(np.mean(cs)), 4))

# ---- 4. approximate optimal instruments, then re-estimate
instrument_results = results.compute_optimal_instruments(method="approximate")
updated_problem = instrument_results.to_problem()
updated = updated_problem.solve(results.sigma, results.pi, optimization=optimization, iteration=iteration, method="1s")
print("== with approximate optimal instruments ==")
print("price coefficient:", np.round(updated.beta.ravel(), 3))
diagnostics(updated, "optimal IV")

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
model_value = float(np.asarray(results.compute_micro_values([placeholder])).ravel()[0])
micro_moment = pyblp.MicroMoment(name="E[income | inside]", value=model_value, parts=income_part)
micro_results = problem.solve(results.sigma, results.pi, optimization=optimization, iteration=iteration,
                              method="1s", micro_moments=[micro_moment])
print("== with one micro moment (target = model-implied value, interface demo only) ==")
print("target", round(model_value, 4), "| re-estimated price coefficient", np.round(micro_results.beta.ravel(), 3))

# ---- optional: the bound trap
if "--show-bound-trap" in sys.argv:
    bounded = problem.solve(sigma0, pi0, optimization=pyblp.Optimization("l-bfgs-b", {"gtol": 1e-6}),
                            iteration=iteration, method="1s")
    print("== same problem with L-BFGS-B and pyblp's default bound diag(sigma) >= 0 ==")
    print("price coefficient:", np.round(bounded.beta.ravel(), 3))
    diagnostics(bounded, "bounded")
    at_bound = np.isclose(np.diag(bounded.sigma), 0.0, atol=1e-10) & ~np.isclose(np.diag(sigma0), 0.0)
    print("sigma diagonal elements stuck at the lower bound 0:", [n for n, b in zip(["1", "prices", "sugar", "mushy"], at_bound) if b])

ok = diag_ok and own_ok and cross_ok and bool((markups > 0).all())
print("CHECKS PASS" if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
