"""结构模型估计的数值自检（只需 numpy 与 scipy）：把 estimation_recipes.md 里的关键结论用小例子复现。

运行：python C:\\Users\\于舒奕\\.claude\\skills\\structural-model-building\\scripts\\structural_selftest.py
全部通过时最后一行打印 ALL PASS。

  T1 动态离散选择：贴现因子 β=0 时退化为静态 logit ................ estimation_recipes.md §3
  T2 嵌套不动点（NFXP）在 β 已知时从模拟数据还原流量效用参数 ...... estimation_recipes.md §3
  T3 模拟矩方差放大 (1 + 1/S)，线性特例 ............................ estimation_recipes.md §2
  T4 Hansen J：工具有效时拒绝率接近名义水平，含无效工具时显著上升 .. estimation_recipes.md §1
  T5 Shapley：各通道贡献加总等于全开减全关 ......................... identification_and_claim_ladder.md §4
  T6 受限基准：先取均值再代入 ≠ 异质模型；方差趋零时异质模型收敛到代表类型 .. when_and_which_model.md §4
  T7 CCP 法（Hotz–Miller）：CCP 映射在真值处是不动点；两步估计还原流量效用参数 .. estimation_recipes.md §3
  T8 一价拍卖：从出价分布反推估值（Guerre–Perrigne–Vuong）......... estimation_recipes.md §7
  T9 生产法加价 = 可变投入产出弹性 ÷ 其收入份额（De Loecker–Warzynski）.. estimation_recipes.md §7
"""
import itertools
import math
import sys

import numpy as np
from scipy import optimize, stats

if hasattr(sys.stdout, "reconfigure"):                    # Windows GBK consoles cannot print β or θ
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

rng = np.random.default_rng(7)
failures = []
EULER = 0.5772156649015329


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        failures.append(name)


# ---------------------------------------------------------------- DDC (Rust-type replacement)
N_STATES = 20
X_GRID = np.arange(N_STATES)


def flow_utils(theta):
    """u(x, keep) = −θ1·x ; u(x, replace) = −θ2. Returns (N_STATES, 2)."""
    return np.column_stack([-theta[0] * X_GRID, -theta[1] * np.ones(N_STATES)])


def transitions():
    """keep: mileage moves up 0/1/2 states with prob .3/.5/.2 (capped); replace: reset to 0 then same move."""
    T_keep = np.zeros((N_STATES, N_STATES))
    for s in range(N_STATES):
        for step, pr in zip((0, 1, 2), (0.3, 0.5, 0.2)):
            T_keep[s, min(s + step, N_STATES - 1)] += pr
    T_rep = np.tile(T_keep[0], (N_STATES, 1))
    return T_keep, T_rep


T_keep, T_rep = transitions()


def logit_rows(v):
    v = v - v.max(axis=1, keepdims=True)
    P = np.exp(v)
    return P / P.sum(axis=1, keepdims=True)


def solve_ccp(theta, beta, tol=1e-12):
    """NFXP inner loop: value iteration on the integrated value function (i.i.d. type-I EV shocks); returns CCPs."""
    u = flow_utils(theta)
    V = np.zeros(N_STATES)
    for _ in range(20000):
        v = u + beta * np.column_stack([T_keep @ V, T_rep @ V])
        m = v.max(axis=1, keepdims=True)
        V_new = (m + np.log(np.exp(v - m).sum(axis=1, keepdims=True))).ravel()
        if np.max(np.abs(V_new - V)) < tol:
            V = V_new
            break
        V = V_new
    return logit_rows(u + beta * np.column_stack([T_keep @ V, T_rep @ V]))


theta_true = np.array([0.25, 3.0])
P_static = logit_rows(flow_utils(theta_true))
check("T1 β = 0: dynamic CCPs equal static logit choice probabilities",
      np.allclose(solve_ccp(theta_true, 0.0), P_static, atol=1e-12))

beta = 0.95
P_true = solve_ccp(theta_true, beta)
n_obs = 20000
states = np.zeros(n_obs, dtype=int)
actions = np.zeros(n_obs, dtype=int)
s = 0
for t in range(n_obs):
    a = int(rng.random() < P_true[s, 1])
    states[t], actions[t] = s, a
    row = T_rep[s] if a == 1 else T_keep[s]
    s = rng.choice(N_STATES, p=row)


def negll(th):
    P = solve_ccp(th, beta, tol=1e-10)
    return -np.log(P[states, actions] + 1e-300).sum()


fit = optimize.minimize(negll, x0=np.array([0.1, 1.5]), method="BFGS")
check("T2 NFXP with β fixed recovers (θ1, θ2) from 20,000 simulated decisions",
      np.allclose(fit.x, theta_true, rtol=0.1), f"estimate {np.round(fit.x, 3)} vs truth {theta_true}")

# ---------------------------------------------------------------- simulated moments variance (linear case)
N, S, R = 400, 2, 3000
est = np.empty(R)
for r in range(R):
    y = 1.0 + rng.normal(size=N)
    eps = rng.normal(size=(N, S))                    # S simulation draws per observation, fixed across θ
    est[r] = (y - eps.mean(axis=1)).mean()           # solves mean(y_i − θ − mean_s ε_is) = 0
ratio = est.var() * N
check("T3 linear special case: simulated-moment estimator variance ≈ (1 + 1/S)·Var(exact moment)",
      abs(ratio - (1 + 1 / S)) < 0.12, f"N·Var = {ratio:.3f} vs {1 + 1 / S:.3f}")


# ---------------------------------------------------------------- Hansen J test
def j_stat(valid=True, n=500):
    z = rng.normal(size=(n, 3))
    u = rng.normal(size=n)
    if not valid:
        u = u + 0.35 * z[:, 2]                       # third instrument enters the error
    x = z @ np.array([1.0, 0.8, 0.6]) + 0.5 * u + rng.normal(size=n)
    yv = 2.0 * x + u
    W = np.linalg.inv(z.T @ z / n)
    b1 = (x @ z @ W @ z.T @ yv) / (x @ z @ W @ z.T @ x)          # first-step 2SLS
    e = yv - b1 * x
    S_hat = (z * e[:, None]).T @ (z * e[:, None]) / n
    W2 = np.linalg.inv(S_hat)
    b2 = (x @ z @ W2 @ z.T @ yv) / (x @ z @ W2 @ z.T @ x)        # efficient two-step GMM
    g = z.T @ (yv - b2 * x) / n
    return n * g @ W2 @ g


crit = stats.chi2.ppf(0.95, df=2)                                    # 3 instruments, 1 parameter
size = np.mean([j_stat(True) > crit for _ in range(600)])
power = np.mean([j_stat(False) > crit for _ in range(300)])
check("T4a Hansen J with valid instruments rejects at about the nominal 5%", 0.02 <= size <= 0.09, f"rejection {size:.3f}")
check("T4b Hansen J rejects much more often when one instrument is invalid", power > 0.5, f"rejection {power:.3f}")

# ---------------------------------------------------------------- Shapley
channels = ["capitalization", "attention", "trust"]


def v_fun(on):
    a, b, c = ("capitalization" in on), ("attention" in on), ("trust" in on)
    return 1.0 * a + 0.5 * b + 0.3 * c + 0.8 * a * b + 0.4 * b * c + 0.6 * a * b * c   # interacting channels


K = len(channels)
phi = {}
for k in channels:
    others = [c for c in channels if c != k]
    tot = 0.0
    for r in range(len(others) + 1):
        for A in itertools.combinations(others, r):
            w = math.factorial(len(A)) * math.factorial(K - len(A) - 1) / math.factorial(K)
            tot += w * (v_fun(set(A) | {k}) - v_fun(set(A)))
    phi[k] = tot
check("T5 Shapley shares sum to v(all on) − v(all off) even with interactions",
      abs(sum(phi.values()) - (v_fun(set(channels)) - v_fun(set()))) < 1e-12,
      ", ".join(f"{k}={phi[k]:.3f}" for k in channels))

# ---------------------------------------------------------------- nested benchmark
G = lambda w: 1.0 / (1.0 + np.exp(-(1.0 - 0.9 * w)))   # nonlinear choice index of a type w (e.g. mileage)
omega_star = 1.2                                        # predetermined representative type of the benchmark
z = rng.normal(size=200000)                             # fixed draws shared by every σ


def full_model(sig):
    """Heterogeneous model: types ω = ω*·exp(σz); the benchmark is the same model at σ = 0."""
    return G(omega_star * np.exp(sig * z)).mean()


omega_hat = omega_star * np.exp(0.8 * z)
check("T6a G(E[ω]) ≠ E[G(ω)]: averaging the type before the nonlinear index is not the heterogeneous model",
      abs(G(omega_hat.mean()) - G(omega_hat).mean()) > 0.01,
      f"G(E[ω])={G(omega_hat.mean()):.4f}, E[G(ω)]={G(omega_hat).mean():.4f}")
gaps = [abs(full_model(sg) - G(omega_star)) for sg in (0.2, 0.1, 0.05)]
check("T6b the benchmark is nested: the full model at σ = 0 equals G(ω*) exactly, and the gap shrinks like σ²",
      full_model(0.0) == G(omega_star) and gaps[0] > gaps[1] > gaps[2] and 3.0 < gaps[1] / gaps[2] < 5.0,
      "gaps " + ", ".join(f"{g_:.2e}" for g_ in gaps))


# ---------------------------------------------------------------- CCP (Hotz–Miller) two-step estimator
def ccp_mapping(theta, P_hat, beta_):
    """Ψ(θ; P̂): value the policy P̂ by one linear solve, then return the logit CCPs it implies."""
    u = flow_utils(theta)
    P_hat = np.clip(P_hat, 1e-10, 1 - 1e-10)
    payoff = (P_hat * (u + EULER - np.log(P_hat))).sum(axis=1)       # E[u_a + ε_a | a chosen] under P̂
    F = P_hat[:, [0]] * T_keep + P_hat[:, [1]] * T_rep                # state transition under P̂
    V = np.linalg.solve(np.eye(N_STATES) - beta_ * F, payoff)
    return logit_rows(u + beta_ * np.column_stack([T_keep @ V, T_rep @ V]))


check("T7a Hotz–Miller: the CCP mapping returns the true CCPs at the true θ (fixed point, no value iteration)",
      np.allclose(ccp_mapping(theta_true, P_true, beta), P_true, atol=1e-10))

# step 1: flexible logit of replacement on a cubic in the state (smooths the rarely visited high states)
Xs = np.column_stack([np.ones(N_STATES), X_GRID / 10, (X_GRID / 10) ** 2, (X_GRID / 10) ** 3])


def first_stage_negll(c):
    idx = Xs @ c
    return -(actions * idx[states] - np.logaddexp(0.0, idx[states])).sum()


c_hat = optimize.minimize(first_stage_negll, np.zeros(4), method="BFGS").x
p_rep = 1 / (1 + np.exp(-(Xs @ c_hat)))
P_hat = np.column_stack([1 - p_rep, p_rep])


# step 2: pseudo-likelihood in θ with P̂ held fixed
def ccp_negll(th):
    P = ccp_mapping(th, P_hat, beta)
    return -np.log(P[states, actions] + 1e-300).sum()


ccp_fit = optimize.minimize(ccp_negll, x0=np.array([0.1, 1.5]), method="BFGS")
check("T7b two-step CCP estimator (flexible-logit first stage, pseudo-likelihood second stage) recovers (θ1, θ2)",
      np.allclose(ccp_fit.x, theta_true, rtol=0.1),
      f"CCP {np.round(ccp_fit.x, 3)} vs NFXP {np.round(fit.x, 3)} vs truth {theta_true}")

# ---------------------------------------------------------------- first-price auction (GPV)
n_bidders, n_auctions = 4, 3000
values = rng.random((n_auctions, n_bidders))                      # i.i.d. private values U[0,1]
bids = ((n_bidders - 1) / n_bidders * values).ravel()             # symmetric BNE bid
b_sorted = np.sort(bids)
h_bw = 1.06 * bids.std() * bids.size ** (-0.2)
grid = np.linspace(0.08, 0.67, 120)                               # interior of the bid support [0, 0.75]
G_hat = np.searchsorted(b_sorted, grid, side="right") / bids.size
g_hat = np.array([np.exp(-0.5 * ((b - bids) / h_bw) ** 2).sum() for b in grid]) / (bids.size * h_bw * np.sqrt(2 * np.pi))
v_pseudo = grid + G_hat / ((n_bidders - 1) * g_hat)              # ξ⁻¹(b) = b + G(b) / [(I−1) g(b)]
v_truth = grid * n_bidders / (n_bidders - 1)
gpv_err = np.abs(v_pseudo - v_truth).mean()
check("T8 GPV inversion recovers private values from the bid distribution alone (interior bids)",
      gpv_err < 0.02, f"mean |v̂ − v| = {gpv_err:.4f}")

# ---------------------------------------------------------------- production-approach markup (DLW)
A_tfp, a_L, b_K, K_cap, wage, eps_d = 2.0, 0.6, 0.3, 5.0, 1.0, 3.0


def profit_foc(L):
    Q = A_tfp * L ** a_L * K_cap ** b_K
    P = Q ** (-1 / eps_d)                                         # constant-elasticity demand
    return (1 - 1 / eps_d) * P * a_L * Q / L - wage                # ∂(PQ)/∂L − w = 0, L chosen after productivity


L_opt = optimize.brentq(profit_foc, 1e-6, 1e6)
Q_opt = A_tfp * L_opt ** a_L * K_cap ** b_K
P_opt = Q_opt ** (-1 / eps_d)
mc = wage * L_opt / (a_L * Q_opt)                                 # w / (∂Q/∂L)
dlw = a_L / (wage * L_opt / (P_opt * Q_opt))                      # output elasticity of L ÷ L's revenue share
check("T9 DLW: elasticity of the variable input ÷ its revenue share equals P/MC (= ε/(ε−1) here)",
      abs(dlw - P_opt / mc) < 1e-9 and abs(dlw - eps_d / (eps_d - 1)) < 1e-9, f"DLW {dlw:.4f}, P/MC {P_opt / mc:.4f}")

print("ALL PASS" if not failures else f"{len(failures)} FAILED: {failures}")
sys.exit(1 if failures else 0)
