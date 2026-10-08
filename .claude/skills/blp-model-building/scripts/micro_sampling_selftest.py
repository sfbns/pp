"""Buyer sampling needs type reweighting; independent synthetic fixture."""
import numpy as np
def main():
    F=np.array([.5,.5])
    P=np.array([[.6,.3,.1],[.05,.15,.8]]) # product1, product2, outside
    PB=1-P[:,-1];sB=F@PB
    FB=F*PB/sB
    correct=(F@P[:,0])/sB
    reweighted=FB@(P[:,0]/PB)
    wrong=F@(P[:,0]/PB)
    assert abs(correct-reweighted)<1e-14
    assert abs(wrong-correct)>.1
    joint=np.zeros((2,3))
    for j in range(2):
        for k in range(3):
            if k!=j:joint[j,k]=F@(P[:,j]*P[:,k]/(1-P[:,j]))/sB
    assert abs(joint.sum()-1)<1e-14
    assert abs(joint[0].sum()-correct)<1e-14
    print(f"[PASS] buyer first-product marginal: correct={correct:.9f}, reweighted={reweighted:.9f}, old-population-integral={wrong:.9f}")
    print(f"[PASS] same-type first/second joint: sum={joint.sum():.9f}, first-product marginal={joint[0].sum():.9f}")
    # Questionnaire which excludes outside from second choices: new set matters.
    conditional_joint=np.zeros((2,2))
    for j in range(2):
        for k in range(2):
            if j!=k:conditional_joint[j,k]=F@(P[:,j]*P[:,k]/(PB-P[:,j]))/sB
    assert abs(conditional_joint.sum()-1)<1e-14
    assert np.max(np.abs(conditional_joint-joint[:,:2]))>.02
    # Survey selection requires inverse selection weights, not duplicated rows.
    selection=np.array([.8,.2]);sample_F=FB*selection;sample_F/=sample_F.sum()
    restored=sample_F/selection;restored/=restored.sum()
    assert np.max(np.abs(restored-FB))<1e-14
    assert abs(sample_F@(P[:,0]/PB)-correct)>.04
    # Two mechanisms with the same index have rank one, not two identified factors.
    z=np.array([1.,2.,3.]);a=.4;gamma=.8
    jac=np.column_stack((a*z,gamma*z))
    assert np.linalg.matrix_rank(jac)==1
    print("[PASS] second-choice outside exclusion, inverse survey weights, and rank-deficient compound-parameter counterexample")
    print("ALL PASS; probability conditioning alone is not type-distribution conditioning")
if __name__=="__main__":main()
