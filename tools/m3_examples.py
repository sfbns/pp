"""Reproducible numeric illustrations for M3 (capitalization of future energy costs). Illustrative [I] only."""
import numpy as np
from scipy.optimize import brentq
from scipy.special import logsumexp

print("== A. present bias: perfect capital market vs hand-to-mouth ==")
beta, r = 0.5, 0.05; dlt = 1/(1+r)
def V_pcm(p, E, W=100.0):
    # perfect capital market, log utility, beta-delta; car price p today, fuel cost E next period
    Y = W - p - E/(1+r); c0 = Y/(1+beta*dlt); c1 = (Y-c0)*(1+r)
    return np.log(c0) + beta*dlt*np.log(c1)
def V_htm(p, E, y0=30.0, y1=30.0):
    return np.log(y0-p) + beta*dlt*np.log(y1-E)
h = 1e-6
for name, V in (("perfect capital market", V_pcm), ("hand-to-mouth (log)", V_htm)):
    g = ((V(10, 5+h)-V(10, 5-h))/(V(10+h, 5)-V(10-h, 5)))/dlt
    print(f"{name:24s}: gamma = {g:.6f}")
print(f"hand-to-mouth prediction beta*u'(c1)/u'(c0) = {beta*(30-10)/(30-5):.6f}; linear utility -> gamma = beta = {beta}")

print("== B. secured car loan: gamma_eff = beta/(1-l+beta*l) ==")
for b in (0.5, 0.7):
    print(f"beta={b}: " + "  ".join(f"l={l:.1f}->{b/(1-l+b*l):.3f}" for l in (0, 0.3, 0.5, 0.8, 1.0)))

print("== C. implied discount rate r*, payback S*, capitalized years gamma*Lambda ==")
Abar = 10
Lam = lambda rate, A=Abar: sum(1/(1+rate)**a for a in range(1, A+1))
L0 = Lam(0.05); gbar = Abar/L0
print(f"Lambda(5%,10)={L0:.4f}; gamma_bar = Lambda(0)/Lambda(r) = {gbar:.4f}")
for g in (0.3, 0.6, 0.9, 1.0, 1.17, 1.3):
    target = g*L0
    rs = brentq(lambda x: Lam(x)-target, -0.2, 5.0)
    Sstar = target   # undiscounted payback with S_a=v_a=1
    print(f"gamma={g:4.2f}: r*={100*rs:7.2f}%  S*={Sstar:6.3f} yrs{' (> Abar)' if Sstar > Abar else ''}  gamma*Lambda={target:.3f}")

print("== D. endogenous attention: fuel-price response reads gamma(3-2gamma) ==")
for th in (0.3, 0.6, 0.9):
    print(f"true theta={th}: fuel-price-based reading = {th*(3-2*th):.3f}")

print("== E. rank of the energy-cost block (normalized singular values) ==")
rng = np.random.default_rng(3); T, J = 40, 10
Kt = 0.2*(1+0.3*rng.standard_normal(T)); Lj = rng.uniform(5, 9, J); Oj = Lj*rng.uniform(1.05, 1.35, J)
xi = rng.normal(0, 0.5, (T, J))
def logsh(theta, two_source=True):
    g, k, z = theta; k = k if two_source else 1.0
    v = xi - g*Kt[:, None]*(k*z*Lj[None, :] + (1-k)*Oj[None, :])
    va = np.c_[np.zeros(T), v]
    return (va - logsumexp(va, axis=1, keepdims=True))[:, 1:].ravel()
def jac(f, t0, h=1e-6):
    t0 = np.asarray(t0, float); f0 = f(t0); Jm = np.zeros((f0.size, t0.size))
    for i in range(t0.size):
        e = np.zeros_like(t0); e[i] = h; Jm[:, i] = (f(t0+e)-f(t0-e))/(2*h)
    return Jm
t0 = [0.7, 0.6, 1.2]
for lab, Jm in (("proportional belief, (gamma,zeta)", jac(lambda t: logsh(t, False), t0)[:, [0, 2]]),
                ("two-source, (gamma,kappa,zeta)", jac(logsh, t0)),
                ("two-source, zeta fixed, (gamma,kappa)", jac(logsh, t0)[:, [0, 1]])):
    sv = np.linalg.svd(Jm/np.linalg.norm(Jm, axis=0), compute_uv=False)
    print(f"{lab:40s}: {np.round(sv, 3)}")

print("== F. welfare: undervaluation wedge vs second-order loss (money metric) ==")
alpha = 5/150000          # utils per yuan
K = 6950.0                # yuan per (L/100km)
Lv = np.array([5.0, 6.0, 7.0, 8.0, 9.0]); xi5 = np.zeros(5)
V = xi5 - alpha*K*Lv*1.0  # true (normative) energy cost part, prices absorbed in xi
V = V - V.mean()          # normalize
def exp_util(gam):
    Vd = V + (1-gam)*alpha*K*(Lv - Lv.mean())     # decision utility undervalues cost differences
    P = np.exp(Vd - logsumexp(Vd))
    return logsumexp(Vd) + P@(V - Vd)
P0 = np.exp(V - logsumexp(V)); varG = P0@((K*Lv)**2) - (P0@(K*Lv))**2
for gam in (0.9, 0.6, 0.3):
    exact = (logsumexp(V) - exp_util(gam))/alpha
    approx = 0.5*(1-gam)**2*alpha*varG
    print(f"gamma={gam}: wedge (1-gamma)K = {(1-gam)*K:7.1f} yuan/(L/100km); loss exact = {exact:7.2f} yuan, 2nd-order approx = {approx:7.2f} yuan")
