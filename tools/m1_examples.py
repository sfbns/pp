import numpy as np
np.set_printoptions(precision=6, suppress=True)

# ---------- Example A: relative utility (homogeneous logit), naive belief ----------
# 3 ICE + 1 BEV, delta_j=0 for inside goods, outside delta0 set to hit target s0.
# Naive belief: Delta u_j = -c * w_j for ICE (w = relative wedge), 0 for BEV.
w = np.array([0.02, 0.12, 0.15, 0.0])
c = 1.26   # = alpha*phi*K*L^N  (utility units per unit relative wedge)
du = -c * w
def shares(delta, delta0):
    e = np.exp(delta); e0 = np.exp(delta0)
    D = e0 + e.sum()
    return e / D, e0 / D
for s0_target in [0.22, 0.58]:
    J = 4
    e0 = s0_target * J / (1 - s0_target)
    d0 = np.log(e0)
    s_old, s0_old = shares(np.zeros(4), d0)
    s_new, s0_new = shares(du, d0)
    lin = s_old * (du - (s_old * du).sum())
    print(f"[A] s0={s0_old:.4f}: du_ICE1={du[0]:.4f}, mean P*du={(s_old*du).sum():.4f}; "
          f"s_ICE1 {s_old[0]:.4f} -> {s_new[0]:.4f} (exact d={s_new[0]-s_old[0]:+.5f}, first-order {lin[0]:+.5f}); "
          f"BEV {s_old[3]:.4f}->{s_new[3]:.4f}; outside {s0_old:.4f}->{s0_new:.4f}")

# ---------- Example B: ratings shrinkage, overall vs subscores ----------
# two subscores k=1,2, weights omega=(0.5,0.5); prior mean 0, prior var sq2_k; noise var se2_k; n reviews
n = 20
qbar = np.array([0.0, 0.0])
sq2 = np.array([0.04, 0.04])     # prior variance of quality
se2 = np.array([0.04, 4.0])      # per-review noise variance (k=2 much noisier)
rbar = np.array([0.30, 0.30])    # observed average subscores (deviation from prior mean)
lam = n*sq2/(n*sq2+se2)          # shrinkage weights
Qk = qbar + lam*(rbar-qbar)
omega = np.array([0.5, 0.5])
sum_omega_Q = (omega*Qk).sum()
# overall score r_all = sum omega_k r_k  -> signal on q_all = sum omega_k q_k; noise var = sum omega^2 se2 / n
sq2_all = (omega**2*sq2).sum()
se2_all = (omega**2*se2).sum()
lam_all = n*sq2_all/(n*sq2_all+se2_all)
Q_all = lam_all*(omega*rbar).sum()
print(f"[B] shrink weights per subscore={lam}, sum omega*Q_k={sum_omega_Q:.4f}; overall-score posterior={Q_all:.4f} (lam_all={lam_all:.4f})")

# ---------- Example C: label diversion and the type structure of the outside option (M1.7) ----------
# Replacers (o_i=1) keep the old car for its remaining life (annuity Lambda0) and then buy a replacement:
#   psi_o - alpha*[phi0*K0_i*e0 + phi0*Kf_i*ef + RC],  K0 ~ Lambda0, Kf ~ Lambda - Lambda0 (horizon-consistent);
# first-time buyers (o_i=0) bear alternative-travel cost over the new car's horizon: -alpha*phi0*c_alt*VKT_i*Lambda.
rng = np.random.default_rng(20261008)
N = 400000
VKT = np.exp(rng.normal(np.log(12000), 0.5, N))          # km/yr
alpha = np.exp(rng.normal(np.log(0.10), 0.3, N))         # utils per 1000 yuan
u_type = rng.random(N)                                   # fixed draw for replacer status
L = np.array([5.0, 6.5, 8.0]); p = np.array([140.0, 120.0, 100.0]); xi = np.ones(3)
pi_f, Lambda, phi, e0, ef, pbar = 7.5, 6.0, 0.8, 8.5, 6.5, 120.0
Ki = pi_f*VKT*Lambda/100/1000                            # 1000 yuan per (L/100km)
def probs(o, Lam0, c_alt, psi_o, shift, cont):
    V = (xi[None, :] + shift) - alpha[:, None]*(p[None, :] + phi*Ki[:, None]*L[None, :])
    K0 = pi_f*VKT*Lam0/100/1000
    Kf = pi_f*VKT*(Lambda - Lam0)/100/1000 if cont else 0.0*VKT
    RC = pbar*(Lambda - Lam0)/Lambda if cont else 0.0    # user cost of the replacement over the remaining years
    Kalt = c_alt*VKT*Lambda/1000                         # 1000 yuan
    V0 = o*(psi_o - alpha*(phi*K0*e0 + phi*Kf*ef + RC)) - (1 - o)*alpha*phi*Kalt
    m = np.maximum(V.max(1), V0); eV = np.exp(V - m[:, None]); e0v = np.exp(V0 - m); D = e0v + eV.sum(1)
    return eV/D[:, None], e0v/D
def bisect(f, lo, hi, it=60):
    for _ in range(it):
        mid = 0.5*(lo + hi)
        if f(mid) > 0: lo = mid
        else: hi = mid
    return 0.5*(lo + hi)
def solve(o_share, Lam0, c_alt, cont, repl_share_buyers=None, target_s0=0.5):
    o = (u_type < o_share).astype(float)
    psi_o = 0.0
    if repl_share_buyers is not None and 0 < o_share < 1:
        # psi_o targets the replacer share among buyers (aggregate micro moment); s0 recalibrated inside
        def gap(ps):
            sh = bisect(lambda s_: probs(o, Lam0, c_alt, ps, s_, cont)[1].mean() - target_s0, -80.0, 120.0, it=40)
            P0 = probs(o, Lam0, c_alt, ps, sh, cont)[1]
            return ((1 - P0)*o).sum()/(1 - P0).sum() - repl_share_buyers
        psi_o = bisect(gap, -20.0, 20.0, it=30)          # replacer share among buyers falls as psi_o rises
    shift = bisect(lambda sh: probs(o, Lam0, c_alt, psi_o, sh, cont)[1].mean() - target_s0, -80.0, 120.0)
    P, P0 = probs(o, Lam0, c_alt, psi_o, shift, cont)
    j = 1; wt = alpha*phi*Ki; den = (wt*P[:, j]*(1 - P[:, j])).mean()
    dL_eff = (wt*P[:, j]*P[:, 0]).mean()/den; dL_out = (wt*P[:, j]*P0).mean()/den
    dsum = sum((wt*P[:, j]*P[:, k]).mean()/den for k in range(3) if k != j) + dL_out
    rep_buy = ((1 - P0)*o).sum()/(1 - P0).sum()
    c_all = np.corrcoef(Ki, P0)[0, 1]
    c_rep = np.corrcoef(Ki[o == 1], P0[o == 1])[0, 1] if o.sum() > 10 else np.nan
    c_fst = np.corrcoef(Ki[o == 0], P0[o == 0])[0, 1] if (1 - o).sum() > 10 else np.nan
    return dict(psi_o=psi_o, s0=P0.mean(), rep_buy=rep_buy, c_all=c_all, c_rep=c_rep, c_fst=c_fst,
                dL_eff=dL_eff, dL_out=dL_out, dsum=dsum)
print("[C] case                                   | psi_o  repl/buyers corr(K,P0): all  replacers first | DR_L->eff DR_L->out  sum")
cases = [("v3: all replacers, Lam0=Lam, no continuation", 1.0, 6.0, 0.0, False, None),
         ("all replacers, Lam0=3, no continuation",       1.0, 3.0, 0.0, False, None),
         ("all replacers, Lam0=3, continuation",          1.0, 3.0, 0.0, True,  None),
         ("50% replacers, Lam0=3, cont., c_alt=0",        0.5, 3.0, 0.0, True,  None),
         ("50% replacers, Lam0=3, cont., c_alt=0.6",      0.5, 3.0, 0.6, True,  None),
         ("same + psi_o to replacer share 0.45",          0.5, 3.0, 0.6, True,  0.45)]
for name, o_sh, Lam0, c_alt, cont, tgt in cases:
    r = solve(o_sh, Lam0, c_alt, cont, tgt)
    print(f"[C] {name:44s} | {r['psi_o']:+6.3f} {r['rep_buy']:.3f}       {r['c_all']:+.3f}  {r['c_rep']:+.3f}   {r['c_fst']:+.3f} "
          f"| {r['dL_eff']:.3f}     {r['dL_out']:.3f}   {r['dsum']:.6f}")

print("== D. supply side: Delta-matrix orientation with product-specific tax factors ==")
from scipy.optimize import fsolve
alpha_d = 0.5
delta_d = np.array([2.0, 1.5, 1.8, 1.2])
vth = np.array([1.13*1.10*1.05, 1.13, 1.13*1.10*1.03, 1.13])   # ICE: VAT, purchase tax, consumption tax; NEV: VAT only
own = np.array([0, 0, 1, 1])                                    # firm 1: products 0,1; firm 2: products 2,3
mc_true = np.array([6.0, 7.0, 6.5, 7.5])
O = (own[:, None] == own[None, :]).astype(float)
def shares_d(ps):
    v = delta_d - alpha_d*vth*ps; e = np.exp(v); return e/(1+e.sum())
def dsdp(ps):                                                   # d s_k / d p_j (consumer price), matrix [j,k]
    s = shares_d(ps); M = alpha_d*np.outer(s, s); M[np.diag_indices(4)] = -alpha_d*s*(1-s); return M
def foc(ps):
    s = shares_d(ps); D = dsdp(ps)
    return np.array([s[j] + sum(O[j, k]*(ps[k]-mc_true[k])*vth[j]*D[j, k] for k in range(4)) for j in range(4)])
ps_eq = fsolve(foc, mc_true*1.3, xtol=1e-12)
s_eq = shares_d(ps_eq); D = dsdp(ps_eq)
Delta = -O*(vth[:, None]*D)                                      # row j: j's price FOC; column k: k's margin
mc_34 = ps_eq - np.linalg.solve(Delta, s_eq)
mc_T = ps_eq - np.linalg.solve(Delta.T, s_eq)
print("equilibrium producer prices:", np.round(ps_eq, 4))
print("mc recovered, BLP (3.4) orientation:", np.round(mc_34, 6), " max error", f"{np.abs(mc_34-mc_true).max():.2e}")
print("mc recovered, transposed orientation:", np.round(mc_T, 6), " max error", f"{np.abs(mc_T-mc_true).max():.4f}")

# ---------- Example E: two ratios R^K (fuel-price variation) and R^L (same-hardware label jump) ----------
# Two-source belief B = kappa*zeta_c*L + (1-kappa)*O (M2), exogenous display timing. Truth R^L = zeta_X/zeta_N.
print("== E. identification source of the revaluation ratio ==")
def twfe(v, g1, g2, it=60):
    v = v.astype(float).copy()
    c1 = np.bincount(g1); c2 = np.bincount(g2)
    for _ in range(it):
        v -= (np.bincount(g1, v)/c1)[g1]; v -= (np.bincount(g2, v)/c2)[g2]
    return v
rngE = np.random.default_rng(7)
J, Tm = 400, 48; aE, gE, kE, zN = 1.0, 0.9, 0.6, 1.0
LN = np.exp(rngE.normal(np.log(7.0), 0.2, J)); wE = rngE.normal(0.077, 0.049, J); LX = LN*(1 + wE)
Ttrue = 1.25*LN*np.exp(rngE.normal(0, 0.08, J)); O = Ttrue*np.exp(rngE.normal(0, 0.05, J))
Tsw = rngE.integers(12, 36, J)
Kt = 1.0 + 0.25*np.sin(np.arange(Tm)/5.0) + 0.05*rngE.normal(size=Tm); Kbar = Kt.mean()
jj, tt = np.meshgrid(np.arange(J), np.arange(Tm), indexing='ij'); jj = jj.ravel(); tt = tt.ravel()
post = tt >= Tsw[jj]
noise = rngE.normal(0, 0.02, jj.size)
cbar = 1/np.mean(1/(1 + wE))                     # 1 + harmonic-mean wedge
for name, zX in (("naive (zeta_X = zeta_N)", zN), ("known average conversion", zN/cbar)):
    Lc = np.where(post, LX[jj], LN[jj]); zc = np.where(post, zX, zN)
    B = kE*zc*Lc + (1 - kE)*O[jj]
    y = -aE*gE*Kt[tt]*B + noise
    est = {}
    for lab, msk, Lv in (("N", ~post, LN), ("X", post, LX)):
        _, ji = np.unique(jj[msk], return_inverse=True); _, ti = np.unique(tt[msk], return_inverse=True)
        Ym = twfe(y[msk], ji, ti); Xm = twfe(Kt[tt[msk]]*Lv[jj[msk]], ji, ti)
        est["K" + lab] = -(Xm @ Ym)/(Xm @ Xm)/aE
    S = post.astype(float)
    X = np.column_stack([twfe((Kt[tt] - Kbar)*Lc, jj, tt), twfe(Kbar*(LX - LN)[jj]*S, jj, tt), twfe(Kbar*LN[jj]*S, jj, tt)])
    b = np.linalg.lstsq(X, twfe(y, jj, tt), rcond=None)[0]
    phiLX = -b[1]/aE; phiLN = phiLX + b[2]/aE
    RK = est["KX"]/est["KN"]; RL = phiLX/phiLN
    print(f"[E] {name}: phi^K_N={est['KN']:.3f}, phi^K_X={est['KX']:.3f}, phi^L_X={phiLX:.3f}, phi^L_N={phiLN:.3f} "
          f"(truth gamma*kappa*zeta: {gE*kE*zX:.3f}, {gE*kE*zN:.3f}); R^K={RK:.3f}, R^L={RL:.3f} (truth {zX/zN:.3f}), "
          f"mixed phi^L_X/phi^K_N={phiLX/est['KN']:.3f}; 1/(1+wbar_harm)={1/cbar:.3f}")

# ---------- Example F: rational-expectations elasticity of beliefs to the new label (M1.16a) ----------
print("== F. RE belief elasticity after relabelling ==")
rngF = np.random.default_rng(3); NF = 2_000_000
for sL, sw, lab in ((0.20, 0.049, "ICE-type wedge dispersion"), (0.20, 0.10, "intermediate"), (0.20, 0.20, "PHEV-type wedge dispersion")):
    lnLN = rngF.normal(np.log(7.0), sL, NF); lnT = lnLN + rngF.normal(np.log(1.25), 0.08, NF)
    lnLX = lnLN + rngF.normal(np.log(1.077), sw, NF)
    bX = np.cov(lnT, lnLX)[0, 1]/np.var(lnLX); bN = np.cov(lnT, lnLN)[0, 1]/np.var(lnLN)
    print(f"[F] {lab}: s_L={sL}, s_w={sw}: slope on ln L^X = {bX:.4f}, formula s_L^2/(s_L^2+s_w^2) = {sL**2/(sL**2+sw**2):.4f}; slope on ln L^N = {bN:.4f}")

# ---------- Example G: exact nesting of M1 in M0 at a representative type (B0) ----------
print("== G. B0 degeneration: M1 at a representative type equals the closed-form logit of M0 ==")
aG, phiG, KG, thG = 0.03, 0.8, 6.95, np.array([1.13*1.10, 1.13, 1.13*1.10])     # alpha per 1000 yuan; K in 1000 yuan/(L/100km)
xG = np.array([1.5, 1.2, 1.0]); pG = np.array([150.0, 130.0, 110.0]); LG = np.array([6.0, 0.0, 7.5]); V0G = -0.5
NS = 1000
draws = np.tile(np.r_[aG], NS)                                  # degenerate type distribution: all draws identical
VG = xG[None, :] - draws[:, None]*(pG[None, :] + phiG*KG*LG[None, :])
PG = np.exp(VG)/(np.exp(V0G) + np.exp(VG).sum(1))[:, None]; sG = PG.mean(0); s0G = 1 - sG.sum()
closed = xG - aG*(pG + phiG*KG*LG)
inv = np.log(sG) - np.log(s0G)
print(f"[G] max |ln s_j - ln s_0 - (V_j - V_0)| = {np.abs(inv - (closed - V0G)).max():.2e}")
dsdp_sim = -(draws[:, None]*PG*(1 - PG)).mean(0); dsdp_cf = -aG*sG*(1 - sG)
print(f"[G] own-price derivative: simulated {np.round(dsdp_sim, 8)} vs closed form {np.round(dsdp_cf, 8)}")
mk = 1/(aG*thG*(1 - sG))                                       # single-product firms: p^s - mc = 1/(alpha*vartheta*(1-s))
Dl = np.diag(-thG*dsdp_cf)
print(f"[G] (M1.47) markups Delta^-1 s = {np.round(np.linalg.solve(Dl, sG), 6)} vs 1/(alpha*vartheta*(1-s)) = {np.round(mk, 6)}")
