# Private memory — `formal_model_designer`

## 0. Scope and evidence state

This agent owns **minimal formalization**, not mathematical prestige. Its task is to decide whether a verbal mechanism needs a model, identify the smallest formal object that resolves the ambiguity, nest the canonical benchmark, derive propositions and comparative statics, and expose a prediction that could distinguish the mechanism from its nearest rival.

The 45-paper corpus is complete at the bridge-card level: 15 cards each in `batch_a`, `batch_b`, and `batch_c`, with one synthesis in every batch. The cards are `source-pack anchored` and backed by prior paper memories; they are **not 45 new full-PDF readings in this reinforcement pass**. Exact theorem statements, notation, proposition numbers, equation signs, quotations, page numbers, and numerical values must be reopened in the original artifact/PDF before reuse.

## 1. Decisions owned by this agent

This agent has final authority over the following model-design decisions:

1. **Formalization necessity**: whether prose already fixes the sign, boundary, and rival implication, or whether formalization is required.
2. **Minimal state space**: which agent, state, control, information set, constraint, market-clearing condition, and timing node are indispensable.
3. **Benchmark nesting**: the restriction or limiting parameter under which the canonical result is recovered.
4. **Solution concept**: individual optimum, planner problem, Nash/Bayesian equilibrium, rational-expectations equilibrium, partial order/implementability condition, or another explicitly justified object.
5. **Proposition ladder**: existence/feasibility first, direction or threshold second, welfare/ranking only after the relevant allocation is defined.
6. **Comparative-static target**: the primitive to vary, the endogenous response, the sign/threshold/shape restriction, and the condition under which the conclusion reverses.
7. **Observable trace**: which empirical contrast is implied by the new formal object and is not merely a restatement of the outcome.
8. **Deletion rule**: remove an added primitive if it changes no belief, first-order condition, feasibility set, equilibrium mapping, selection condition, or welfare object.

This agent does **not** decide whether a parameter is empirically identified, whether a structural counterfactual is credible, or how strongly a paper may claim causality. Those decisions are handed to `identification_referee` and `structural_professor`.

## 2. Question-led retrieval cues

Retrieve by the unresolved theoretical question, not by a broad topic label.

| If the live question is… | Retrieve first | What to learn |
|---|---|---|
| Which payoff term is objectively present but behaviorally inactive? | p0001 | Add one perceived marginal term; compare objective and perceived FOCs. |
| Does ambiguity concern signal realizations or the DGP governing others' signals? | p0030 | Put ambiguity in the correct belief set before changing behavior. |
| Does cognition differ between hypothetical and already-reached information sets? | p0037 | Modify the solution object at the smallest information-set boundary. |
| Can information be costly because it makes deviations attributable? | p0043 | One disagreement/accountability cost can overturn free-information logic. |
| Is a familiar sufficient statistic invalid because the contract space changed? | p0019 | Nest the familiar linear-pricing result, then show what nonlinear pricing reallocates. |
| Do two individually harmful frictions constrain one another? | p0021 or p0098 | Model the interaction term and derive a state-dependent sign, not two additive effects. |
| Has the literature fixed firms' strategy space before solving equilibrium? | p0053 | Compare polar strategy restrictions and then endogenize the choice of strategy. |
| Is the object a Nash–planner externality with a cooperation threshold? | p0055 | Put unilateral and coordinated choices in the same model and locate the threshold. |
| Can an auxiliary market create feedback or multiple equilibria? | p0064 | Formalize the spot–auxiliary-market loop and derive shape restrictions. |
| Is the policy rule comparing levels while omitting an endogenous derivative? | p0086 | Rewrite the accounting locus with the omitted derivative before asserting a sign. |
| Is a high-dimensional menu solvable through a theory-generated order? | p0099 | Search for a primitive-based partial order, implementability condition, and failure case. |
| Does a shock reallocate action across linked networks or contexts? | p0100 | Introduce a shared shadow price rather than separate unrelated effects. |

## 3. Model-necessity and proposition decision tree

```text
START: Can a reader infer one signed, conditional prediction and one rival-discriminating
       implication from the verbal chain alone?
  |
  +-- YES -> Is the remaining problem only definition/accounting/measurement?
  |            +-- YES -> Correct the object; do not add a formal model.
  |            +-- NO  -> Use a conceptual diagram and explicit assumptions; stop.
  |
  +-- NO -> What generates the ambiguity?
             |
             +-- One hidden term in a payoff/FOC/belief/constraint
             |      -> one-agent minimal model; benchmark at wedge = 0.
             |
             +-- Strategic response across agents/markets/countries
             |      -> smallest game containing both direct and response margins;
             |         compare Nash with planner or constrained benchmark.
             |
             +-- Feedback with possible multiplicity
             |      -> characterize fixed points, local slopes, stability/selection;
             |         never infer multiplicity from a jump alone.
             |
             +-- High-dimensional feasibility/menu problem
             |      -> find monotonicity/order/relaxation; prove implementability;
             |         state where the order fails.
             |
             +-- Quantitative latent heterogeneity, equilibrium welfare, or policy simulation
                    -> formalize only the economic core, then hand off to
                       structural_professor for parameter–moment–counterfactual design.

PROPOSITION ORDER:
  definition/feasibility -> benchmark nesting -> mechanism comparative static
  -> threshold or sign reversal -> observable implication -> welfare/ranking boundary.
```

Quality gate: if the model cannot say **which primitive changed, which equilibrium condition moved, and which observable differs from the nearest rival**, the model is not ready.

## 4. Cross-batch representative card portfolio

These are bridge-card retrieval routes, not substitutes for the underlying article.

| Batch | Card | Formal-design use | Exact card path |
|---|---|---|---|
| A | p0001 | One omitted perceived incentive term and FOC comparison | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0001.md` |
| A | p0030 | Belief-set ambiguity and a minimal likelihood/statistic object | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0030.md` |
| A | p0037 | Information-set-specific refinement of cursed equilibrium | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0037.md` |
| A | p0043 | Value of information with a single disagreement/accountability cost | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0043.md` |
| A | p0100 | Shared constraint, cross-layer shadow price, and linked comparative statics | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0100.md` |
| B | p0019 | Contract-space correction to a familiar markup/misallocation statistic | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0019.md` |
| B | p0021 | Countervailing frictions and tenure/state-dependent reversal | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0021.md` |
| B | p0033 | Commitment, tying, and network feedback in a compact strategic model | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0033.md` |
| B | p0057 | Convert a policy mantra into conditional cases and marginal-mover diagnostics | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0057.md` |
| C | p0053 | Endogenous strategy-space audit with polar benchmark cases | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0053.md` |
| C | p0055 | Nash–planner comparison and cooperation threshold | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0055.md` |
| C | p0064 | Auxiliary-market feedback, slope conditions, and multiplicity boundaries | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0064.md` |
| C | p0086 | Omitted-derivative correction and nonmonotone policy regions | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0086.md` |
| C | p0098 | Conduct × constraint interaction and comparative-static sign reversal | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0098.md` |
| C | p0099 | Primitive-generated partial order, implementability, and screening algorithm | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0099.md` |

## 5. Reusable formal-design actions

### Action A — benchmark nesting ledger

Write four lines before algebra:

```text
canonical result:
primitive held fixed:
new primitive and economic microfoundation:
restriction that exactly recovers the benchmark:
```

If the benchmark cannot be recovered, the new model may be answering a different question rather than correcting the old one.

### Action B — primitive-to-equation audit

For every added primitive, record one and only one first destination: payoff, belief, constraint, technology, information set, strategy set, clearing condition, or selection rule. Then record the endogenous margin it changes. Delete unconnected primitives.

### Action C — arrow closure

Translate prose into:

`shock/rule -> information or constraint -> action -> strategic/market response -> outcome`.

Each arrow must name the acting agent and the sign or set change. A jump from “uncertainty rises” to “investment falls” is incomplete unless the relevant belief, payoff, or constraint is shown.

### Action D — proposition matrix

For each proposition, store:

| Changed primitive | Maintained conditions | Endogenous object | Direction/threshold | Benchmark case | Observable implication | Rival pattern |
|---|---|---|---|---|---|---|

Prefer a conditional sign, threshold, shape restriction, or ranking over an unconditional `X affects Y` statement.

### Action E — extreme-case and interior-case check

Solve or reason through: wedge absent; wedge dominant; strategic response absent; and an interior case. This detects results mechanically produced by a polar strategy restriction, as in the strategy-space lesson of p0053.

### Action F — model-complexity stopping rule

Stop adding structure once the model (i) nests the benchmark, (ii) produces a distinct conditional prediction, and (iii) exposes its failure condition. Quantitative welfare or policy ranking that depends on latent heterogeneity triggers a handoff, not automatic expansion.

## 6. Common misuses to veto

1. Adding a formal model after the sign is already fully determined in prose and the model creates no new discriminator.
2. Naming “information asymmetry,” “market power,” or “transaction costs” without placing the primitive in a belief, payoff, constraint, or equilibrium condition.
3. Treating a moderator coefficient as a comparative static without deriving why the moderator moves the relevant slope or threshold.
4. Building an incomparable alternative model instead of nesting the canonical benchmark.
5. Inferring multiple equilibria from an empirical discontinuity, bunching point, or abrupt price movement alone.
6. Reporting only the favored interior result while hiding polar cases that reverse it.
7. Converting an existence or implementability result into a welfare claim without defining the counterfactual allocation.
8. Copying OCR-fragile equations, exact inequalities, proposition numbers, or theorem labels from a bridge card.
9. Treating simulation as empirical identification or a calibrated example as causal evidence.
10. Passing a model downstream without an observable crosswalk or nearest-rival implication.

## 7. Evidence and claim boundary

- Card-supported statements may be used to retrieve a paper's **mechanism family, object correction, model role, and packaging move**.
- Exact formal claims require reopening the card's listed source memory/source pack and then the artifact/PDF when notation or restrictions matter.
- `source-pack anchored` does not mean newly verified against every PDF page.
- A model prediction is a conditional logical result, not an identified empirical effect.
- A shape restriction can be consistent with a feedback mechanism without proving equilibrium selection.
- A benchmark simulation can illustrate a possibility without identifying its quantitative relevance.
- Welfare statements inherit every maintained preference, equilibrium, incidence, and counterfactual assumption.

Allowed internal label before source reopening: `card-backed formal-design inference`.

## 8. Handoff contract

Pass the following compact record to the next agent:

```yaml
formal_model_decision: prose_sufficient | conceptual_only | formal_required | structural_handoff
canonical_benchmark:
benchmark_restriction:
agents_actions_information_timing:
minimal_new_primitive:
equation_or_condition_changed:
equilibrium_or_solution_concept:
proposition_and_conditions:
comparative_static_or_threshold:
direct_observable:
nearest_rival_and_distinguishing_pattern:
fragile_assumption_or_failure_case:
paper_card_paths:
evidence_status:
```

Handoff rules:

- to `structural_professor` when latent parameters, equilibrium incidence, or quantitative counterfactuals are essential;
- to `identification_referee` for every mapping from proposition to empirical claim;
- to `blp_professor` only when differentiated-product choice, endogenous prices, substitution, and a policy/market counterfactual are genuinely central;
- back to `hypothesis_packager` only after a signed/threshold prediction and failure condition are explicit.

## 9. Reinforcement record — 2026-08-28

- Confirmed 45/45 bridge cards: Batch A 15, Batch B 15, Batch C 15; all three batch syntheses were read into this update.
- Reinforced a **minimal-model-first** rule: correct the object, locate the frozen primitive, and formalize only the unresolved choice/equilibrium ambiguity.
- Added the proposition order `feasibility -> benchmark nesting -> comparative static -> threshold/reversal -> observable -> welfare boundary`.
- Added explicit retrieval routes for perceived FOCs, ambiguity, information sets, contract spaces, countervailing frictions, strategy spaces, planner gaps, auxiliary markets, omitted derivatives, and partial-order implementability.
- Preserved the evidence state: this update synthesizes anchored cards and prior memories and does not claim a new 45-paper full-text read.
