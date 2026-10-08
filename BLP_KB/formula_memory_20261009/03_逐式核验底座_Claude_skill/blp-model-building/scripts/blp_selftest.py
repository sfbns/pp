"""BLP 数值自检：把本 skill 里最容易抄错的八处用数字核一遍（只需 numpy）。

运行：python C:\\Users\\于舒奕\\.claude\\skills\\blp-model-building\\scripts\\blp_selftest.py
全部通过时最后一行打印 ALL PASS；任何一条失败都会报出是哪一条、差多少。

对应 skill 文件：
  T1 (6.9b) 前置负号与 ∂μ_iq/∂p_q ........ references/blp1995_verified_equations.md、micro_foundations.md §4(c)
     （T1c、T1d 把两种照抄写法与有限差分 Jacobian 对比，导数 ∂μ/∂p 由模型数值求出，不是手填）
  T2 Δ 方向（BLP (3.4) 与 Conlon–Gortmaker 式 (6)）.... micro_foundations.md §7(c)
  T3 单产品 logit 加价 1/[α(1−s)] ........ micro_foundations.md §7(b)（先用数值导数解出 Bertrand 均衡，再对闭式）
  T4 GHvB 边界式与期刊版表 7 .............. extension_genealogy.md B1
  T5 Alé-Chilet 等式 (13) 的符号 .......... extension_genealogy.md S3
  T6 Small–Rosen logsum = 期望最大效用 ..... micro_foundations.md §8
  T7 续航缺口 A(R)=E[(D−R)+] 的一二阶导 ..... project_china_driving_cycle.md §15、estimation 配方 4
  T8 均值之比 E[θ/δ] ≠ E[θ]/E[δ] .......... extension_genealogy.md B1
"""
import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):                    # Windows GBK consoles cannot print ∂ or μ
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

rng = np.random.default_rng(20261007)
failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        failures.append(name)


def mixed_logit_probs(delta, mu):
    """Individual choice probabilities P_ij with outside option utility 0. delta: (J,), mu: (I,J)."""
    u = delta[None, :] + mu
    m = np.maximum(u.max(axis=1, keepdims=True), 0.0)
    e = np.exp(u - m)
    return e / (np.exp(-m) + e.sum(axis=1, keepdims=True))


# ---------------------------------------------------------------- common market
J, I = 4, 4000
x = rng.normal(size=J)
p = np.array([1.0, 1.6, 2.2, 2.8])
alpha, beta, sigma = 2.0, 0.6, 0.9
y = 3.5 + np.exp(rng.normal(1.2, 0.5, size=I))          # incomes above all prices
nu = rng.normal(size=I)
firm = np.array([0, 0, 1, 1])                            # two two-product firms
H = (firm[:, None] == firm[None, :]).astype(float)


def shares_income(prices):
    """BLP (2.7a)-style income spec: u_ij = α log(y_i − p_j) + βx_j + σ x_j ν_i + ε_ij (outside: α log y_i)."""
    mu = alpha * (np.log(y[:, None] - prices[None, :]) - np.log(y)[:, None]) + sigma * np.outer(nu, x)
    P = mixed_logit_probs(beta * x, mu)
    return P.mean(axis=0), P


def shares_quasilinear(prices, a_i):
    mu = -np.outer(a_i, prices) + sigma * np.outer(nu, x)
    P = mixed_logit_probs(beta * x, mu)
    return P.mean(axis=0), P


def fd_jacobian(fun, prices, h=1e-6):
    """J[j, k] = ∂s_j/∂p_k by central differences."""
    out = np.zeros((len(prices), len(prices)))
    for k in range(len(prices)):
        up, dn = prices.copy(), prices.copy()
        up[k] += h
        dn[k] -= h
        out[:, k] = (fun(up)[0] - fun(dn)[0]) / (2 * h)
    return out


# ---------------------------------------------------------------- T1 (6.9b)
s, P = shares_income(p)
dmu = -alpha / (y[:, None] - p[None, :])                 # ∂μ_iq/∂p_q (negative)
J_an = np.zeros((J, J))
for j in range(J):
    for q in range(J):
        if j == q:
            J_an[j, q] = np.mean(P[:, j] * (1 - P[:, j]) * dmu[:, j])          # (6.9a)
        else:
            J_an[j, q] = np.mean(-P[:, j] * P[:, q] * dmu[:, q])              # (6.9b) corrected
J_fd = fd_jacobian(shares_income, p)
check("T1a (6.9a)/(6.9b) with leading minus and ∂μ_iq/∂p_q match finite differences",
      np.allclose(J_an, J_fd, atol=1e-7), f"max abs diff {np.abs(J_an - J_fd).max():.2e}")
off = ~np.eye(J, dtype=bool)
check("T1b cross-price derivatives are positive (substitutes)", bool((J_an[off] > 0).all()))


def mu_income(prices):
    """The individual-specific part μ_ij of the income spec, as a function of all prices (I x J)."""
    return alpha * (np.log(y[:, None] - prices[None, :]) - np.log(y)[:, None]) + sigma * np.outer(nu, x)


# ∂μ_ij/∂p_q computed numerically from the model, for every (j, q) pair: dmu_num[:, j, q]
h_mu = 1e-6
dmu_num = np.zeros((I, J, J))
for q in range(J):
    up, dn = p.copy(), p.copy()
    up[q] += h_mu
    dn[q] -= h_mu
    dmu_num[:, :, q] = (mu_income(up) - mu_income(dn)) / (2 * h_mu)
# (6.9b) as printed but without the leading minus, using the correct subscript μ_iq
J_nominus = np.array([[np.mean(P[:, j] * P[:, q] * dmu_num[:, q, q]) if j != q else J_fd[j, q]
                       for q in range(J)] for j in range(J)])
check("T1c (6.9b) without the leading minus disagrees in sign with the finite-difference Jacobian everywhere off the diagonal",
      bool((np.sign(J_nominus[off]) != np.sign(J_fd[off])).all()),
      f"min |FD cross| {np.abs(J_fd[off]).min():.2e}")
# (6.9b) with the minus but the printed subscript μ_ij: ∂μ_ij/∂p_q is computed from the model, not typed in
J_printed_sub = np.array([[np.mean(-P[:, j] * P[:, q] * dmu_num[:, j, q]) if j != q else J_fd[j, q]
                           for q in range(J)] for j in range(J)])
check("T1d (6.9b) with the printed subscript ∂μ_ij/∂p_q gives zero cross derivatives, while finite differences are positive",
      bool(np.allclose(J_printed_sub[off], 0.0) and (J_fd[off] > 1e-4).all()),
      f"max |printed-subscript cross| {np.abs(J_printed_sub[off]).max():.1e}")

# ---------------------------------------------------------------- T2 Δ direction
asym = np.abs(J_an - J_an.T).max()
check("T2a income spec: demand Jacobian is NOT symmetric", asym > 1e-4, f"max|J−Jᵀ| = {asym:.4f}")
Delta_blp = -(H * J_an.T)          # BLP (3.4): Δ_jr = −∂s_r/∂p_j
Delta_cg = -(H * J_an)             # Conlon–Gortmaker eq.(6) read literally: (j,k) = ∂s_j/∂p_k
markup = np.linalg.solve(Delta_blp, s)
mc = p - markup
foc = s + np.array([sum(H[j, r] * (p[r] - mc[r]) * J_an[r, j] for r in range(J)) for j in range(J)])
check("T2b markups from BLP Δ satisfy the Bertrand FOC s_j + Σ_r (p_r−mc_r)∂s_r/∂p_j = 0",
      np.abs(foc).max() < 1e-12, f"max |FOC| = {np.abs(foc).max():.1e}")
res_cg = np.abs(s - Delta_cg @ (p - mc)).max()
check("T2c the untransposed Δ violates the FOC when J is asymmetric", res_cg > 1e-4, f"residual {res_cg:.2e}")
a_i = np.exp(rng.normal(0.5, 0.3, size=I))
J_ql = fd_jacobian(lambda pr: shares_quasilinear(pr, a_i), p)
check("T2d quasi-linear price: Jacobian symmetric, so both Δ versions coincide",
      np.abs(J_ql - J_ql.T).max() < 1e-7, f"max|J−Jᵀ| = {np.abs(J_ql - J_ql.T).max():.1e}")

# ---------------------------------------------------------------- T3 logit markup
a = 1.3
d = np.array([0.4, -0.2, 0.1])
mc3 = np.array([1.0, 0.8, 1.2])


def logit_shares(prices):
    e = np.exp(d - a * prices)
    return e / (1 + e.sum())


def own_derivative_fd(prices, h=1e-6):
    out = np.zeros(len(prices))
    for j in range(len(prices)):
        up, dn = prices.copy(), prices.copy()
        up[j] += h
        dn[j] -= h
        out[j] = (logit_shares(up)[j] - logit_shares(dn)[j]) / (2 * h)
    return out


# solve the single-product Bertrand equilibrium using only numerical derivatives of the share function
pr = mc3 + 1.0
for _ in range(5000):
    pr_new = mc3 - logit_shares(pr) / own_derivative_fd(pr)
    if np.abs(pr_new - pr).max() < 1e-12:
        break
    pr = pr_new
sh = logit_shares(pr)
check("T3 Bertrand equilibrium solved with finite-difference derivatives has markups p−mc = 1/[α(1−s)]",
      np.allclose(pr - mc3, 1 / (a * (1 - sh)), atol=1e-6),
      f"max diff {np.abs(pr - mc3 - 1 / (a * (1 - sh))).max():.1e}")

# ---------------------------------------------------------------- T4 GHvB bound
dP, P0 = -294.0, 24500.0                                  # equilibrium price fell by $294
table7 = {(-0.05, -6): 498, (-0.05, -4): 600, (-0.01, -6): 335, (-0.01, -4): 355, (0.05, -6): 90, (0.05, -4): -12}
ok = True
for (dq, eta), wtp in table7.items():
    dwtp = dP - P0 * dq / eta                             # signed: ΔWTP = ΔP − P0·(ΔQ/Q)/η_D
    ok &= abs(-dwtp - wtp) <= 1.0
check("T4a ΔWTP = ΔP − P0·(ΔQ/Q)/η_D reproduces all six cells of GHvB (2021) Table 7", ok)
wrong = [dP + dP * dq / eta for (dq, eta) in table7]
check("T4b the working-paper footnote-26 version ΔP + ΔP·ΔQ/η_D stays near −294 (typo)",
      max(abs(w - dP) for w in wrong) < 4.0)
# NBER w25845 Table D.1 (D:\fuel-econ-lit-2026\raw_text\P17_w25845.txt, PAGE 52): its note says P = 24,500,
# but the ten cells are reproduced by the post-shock price 24,500 − 294 = 24,206.
tableD1 = {(-0.05, -6): 496, (-0.05, -4): 597, (-0.01, -6): 334, (-0.01, -4): 355, (0.0, -6): 294,
           (0.0, -4): 294, (0.01, -6): 254, (0.01, -4): 233, (0.05, -6): 92, (0.05, -4): -9}
P1 = P0 + dP
check("T4c the same formula with P1 = 24,206 reproduces all ten cells of working-paper Table D.1",
      all(abs(-(dP - P1 * dq / eta) - wtp) <= 1.0 for (dq, eta), wtp in tableD1.items()))

# ---------------------------------------------------------------- T5 Alé-Chilet sign
S_ac = -J_an.T                                            # S_jh = −∂s_h/∂p_j (their definition)
mc_minus = p - np.linalg.solve(H * S_ac, s)
mc_plus = p + np.linalg.solve(H * S_ac, s)
check("T5a with S_jh = −∂s_h/∂p_j, mc = p − (Ω⊙S)⁻¹s equals the BLP marginal cost", np.allclose(mc_minus, mc))
check("T5b the printed plus sign gives mc > p for every product", bool((mc_plus > p).all()))

# ---------------------------------------------------------------- T6 Small–Rosen logsum
V = np.array([0.0, 0.7, -0.3, 1.1])
draws = rng.gumbel(size=(400000, V.size))
emax = (V[None, :] + draws).max(axis=1).mean()
logsum = np.log(np.exp(V).sum()) + np.euler_gamma
check("T6 E[max_j(V_j+ε_j)] = log Σ exp V_j + Euler γ (i.i.d. type-I EV)", abs(emax - logsum) < 0.01,
      f"sim {emax:.4f} vs {logsum:.4f}")

# ---------------------------------------------------------------- T7 range gap
Dtrip = np.exp(rng.normal(np.log(120.0), 0.6, size=2_000_000))   # trip-distance draws (km)
R, h = 200.0, 2.0
A = lambda r: np.maximum(Dtrip - r, 0.0).mean()
dA = (A(R + h) - A(R - h)) / (2 * h)
d2A = (A(R + h) - 2 * A(R) + A(R - h)) / h ** 2
pr_gt = (Dtrip > R).mean()
dens = ((Dtrip > R - h) & (Dtrip <= R + h)).mean() / (2 * h)
check("T7a A′(R) = −Pr(D > R)", abs(dA + pr_gt) < 2e-3, f"{dA:.4f} vs {-pr_gt:.4f}")
check("T7b A″(R) = f_D(R) ≥ 0, so −κA(R) gives positive, diminishing marginal value of range",
      abs(d2A - dens) < 5e-4 and d2A >= 0, f"{d2A:.5f} vs {dens:.5f}")

# ---------------------------------------------------------------- T8 ratio of means
# δ_i: heterogeneous marginal utility of money; θ_i: fuel-cost weight not proportional to δ_i
delta_i = np.exp(rng.normal(0.0, 0.5, size=1_000_000))
theta_i = 0.4 * np.exp(rng.normal(0.0, 0.3, size=delta_i.size))
exact = np.mean(theta_i / delta_i)
ratio = theta_i.mean() / delta_i.mean()
approx = ratio - np.cov(delta_i, theta_i)[0, 1] / delta_i.mean() ** 2 + delta_i.var() * theta_i.mean() / delta_i.mean() ** 3
check("T8a E[θ/δ] differs from E[θ]/E[δ] when the price coefficient is heterogeneous", abs(exact - ratio) > 0.01,
      f"E[θ/δ]={exact:.4f}, E[θ]/E[δ]={ratio:.4f}")
check("T8b the second-order correction moves E[θ]/E[δ] toward E[θ/δ]", abs(approx - exact) < abs(ratio - exact),
      f"corrected {approx:.4f}")

print("ALL PASS" if not failures else f"{len(failures)} FAILED: {failures}")
sys.exit(1 if failures else 0)
