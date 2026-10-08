"""Two sampling designs, two counting rules; synthetic check, no data estimate."""
import numpy as np
def main():
    ns=4;sbar=.6;fbar=np.full(ns,.6);fj=np.full(ns,.3)
    raw=float(np.sum(sbar/fbar*fj))
    accepted=float(np.mean(sbar/fbar*fj))
    assert abs(raw-1.2)<1e-12 and abs(accepted-.3)<1e-12
    rng=np.random.default_rng(6101);N=500000
    proposed=(rng.random(N)<.6).astype(float)
    attempt=float(np.mean(proposed*.3/.6))
    assert abs(attempt-.3)<.002
    print(f"[PASS] fixed accepted count: printed sum={raw:.6f}; mean={accepted:.6f}")
    print(f"[PASS] fixed proposal count: inverse-probability estimate={attempt:.6f}; target=0.300000")
    # Nonconstant acceptance probabilities: tests distinguish the measures.
    p0=np.array([.4,.6]);fb=np.array([.2,.8]);fj2=np.array([.15,.28])
    sb=float(p0@fb);q=p0*fb/sb;truth=float(p0@fj2)
    accepted_exact=float(q@(sb/fb*fj2))
    proposal_exact=float(p0@(fb*fj2/fb))
    wrong_extra=float(accepted_exact/sb)
    assert abs(truth-.228)<1e-14
    assert abs(accepted_exact-truth)<1e-14 and abs(proposal_exact-truth)<1e-14
    assert abs(wrong_extra-truth)>.17
    # Both real sampling designs, fixed independent seeds and counting rules.
    types=rng.choice(2,N,p=p0);accept=rng.random(N)<fb[types]
    proposal_mc=float(np.mean(accept*fj2[types]/fb[types]))
    accepted_types=rng.choice(2,N,p=q)
    accepted_mc=float(np.mean(sb/fb[accepted_types]*fj2[accepted_types]))
    assert abs(proposal_mc-truth)<.002 and abs(accepted_mc-truth)<.002
    print(f"[PASS] nonconstant two-type exact: sbar={sb:.6f}; target={truth:.6f}; accepted={accepted_exact:.6f}; proposal={proposal_exact:.6f}; withdrawn-extra-division={wrong_extra:.6f}")
    print(f"[PASS] nonconstant two-type simulations: accepted={accepted_mc:.6f}; proposal={proposal_mc:.6f}")
    print("ALL PASS; different counting rules are not interchangeable")
if __name__=="__main__":main()
