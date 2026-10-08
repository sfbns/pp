# Top-journal research protocol

Use this protocol for idea generation, research design, referee review, structural-model choice, and contribution framing. It distills recurring moves from 100 AER third-pass memories and 107 AEJ second-pass cards. Treat those memories as a pattern library; do not treat corpus frequency as a quality rule or a novelty claim.

## Route the two corpora differently

| Need | First corpus layer | What it contributes |
|---|---|---|
| Correct the theoretical, welfare, equilibrium, or estimand object | AER third-pass global synthesis, manifest, then per-paper memory | Object correction, canonical-model discipline, structural necessity, counterfactual boundaries |
| Diagnose policy implementation or empirical leverage | AEJ second-pass synthesis and cards | Institutional wedges, discretion, hidden measurement, heterogeneity, adaptation, policy incidence |
| Find an introduction or story architecture | AER/AEJ card fields | Story ladder, framework, innovation source, reusable move |
| Make a paper-specific factual claim | Per-paper memory, source pack, OCR artifact, then clean PDF where consequential | Source grounding and claim boundaries |

Start with:

```powershell
python D:\codex\.codex-home\skills\economics-expert-reviewer\scripts\find_top_journal_memory.py --query "implementation discretion"
python D:\codex\.codex-home\skills\economics-expert-reviewer\scripts\find_top_journal_memory.py --query "equilibrium welfare" --corpus aer
python D:\codex\.codex-home\skills\economics-expert-reviewer\scripts\find_top_journal_memory.py --tag spillover --corpus aej
```

Open only the closest few records. Do not preload the four-million-character AER synthesis when an index or one paper memory is sufficient.

## Apply the object-wedge test

Build the research logic in this order:

1. `Visible object`: What outcome, treated unit, policy, market, coefficient, or canonical model does the debate currently use?
2. `Omitted wedge`: Which institutional or economic margin could make that object incomplete?
3. `Corrected object`: What should actually be explained, estimated, or valued once the wedge is admitted?
4. `Mechanism`: Which agents change which actions because which constraint, information set, price, belief, or incentive changes?
5. `Observable mapping`: What directly measures each object, and what is only a proxy?
6. `Estimand`: What population, comparison, horizon, treatment version, equilibrium regime, and welfare/incidence object are targeted?
7. `Identification`: Which variation recovers the estimand, under which assumptions?
8. `Interpretation`: What conclusion survives after close alternatives and boundary conditions are considered?

If the project cannot state a corrected object or a consequential wedge, it may be a topic, dataset, or method application rather than a research contribution.

## Stress-test eight recurring wedges

Use only wedges that fit the institution.

| Wedge | Diagnostic question | Stronger design response |
|---|---|---|
| Implementation and gatekeepers | Who interprets, allocates, enforces, or can quietly attenuate the rule after adoption? | Measure treatment versions, compliance, discretion, and intermediary behavior |
| Wrong outcome or treated unit | Is the headline outcome only one layer of incidence or welfare? | Follow downstream units, adjacent markets, substitution, and distribution |
| Hidden measurement object | Is the causal question blocked because the key economic object is latent or spatially mismeasured? | Build and validate the object before estimating effects |
| Heterogeneity as mechanism | Which constraint or type makes the effect appear, disappear, or reverse? | Pre-specify theory-linked heterogeneity; avoid decorative subgroup mining |
| Strategic adaptation | What margin opens when the policy closes another? | Trace substitution, gaming, anticipation, relocation, or avoidance |
| Dynamics | Does a static estimate miss adjustment costs, learning, state dependence, or long-run selection? | Align horizon and treatment history with the mechanism |
| Equilibrium and spillovers | Do prices, congestion, entry, sorting, networks, or market composition feed back on the direct effect? | Define the equilibrium exposure and distinguish direct from total effects |
| Benchmark reversal | Which primitive assumed fixed by the canonical model is variable here? | State the benchmark, change one disciplined primitive, and derive a discriminating prediction |

## Make mechanisms auditable

Write each mechanism as a chain rather than a label:

`shock or rule -> agent information/constraint/incentive -> action -> market or institutional response -> measured outcome`

For every arrow, record:

- the economic object;
- the observable or experimental contrast;
- the identifying assumption, if causal;
- the closest alternative channel;
- a result that would weaken or falsify the proposed link.

Heterogeneity supports a mechanism only when the splitting variable is fixed by theory and distinguishes close channels. A downstream association alone is mechanism-consistent evidence, not identified mediation.

## Choose reduced form, formal theory, or structure

Use reduced form when the target is a local causal effect or a design diagnostic and the intended claim does not require equilibrium reconstruction.

Add a formal model when one primitive generates distinctive predictions, organizes otherwise ambiguous mechanisms, or defines an economic object that prose cannot discipline.

Require a structural model only when the user needs a named counterfactual, welfare decomposition, equilibrium allocation, dynamic response, targeting rule, menu design, or market-level feedback. State:

- states, agents, actions, information, shocks, and timing;
- equilibrium concept and welfare/incidence object;
- which variation identifies each parameter or object;
- computation and validation targets;
- which counterfactual cannot be answered by reduced form.

Do not default to BLP. Use it only when differentiated-product demand, market shares, substitution patterns, endogenous prices, and product-market welfare counterfactuals are central.

## Screen ideas before polishing

An idea is ready for development only if it passes all six screens:

1. `Object`: the corrected object is economically consequential.
2. `Wedge`: the omitted margin is institutionally real, not an invented story.
3. `Measurement`: key objects have defensible observables or a credible construction plan.
4. `Identification`: usable variation targets the stated estimand.
5. `Discrimination`: evidence can separate the mechanism from close substitutes.
6. `Contribution`: the result would revise a theory, policy evaluation, welfare object, or accepted empirical interpretation even if the coefficient is modest.

Label an idea `promising but unverified` until the closest literature and data feasibility are checked. Top-journal resemblance is not evidence of novelty.

## Translate the protocol into review findings

For each material problem, report:

- `failure`: the exact object, link, or assumption that breaks;
- `consequence`: which contribution or conclusion no longer follows;
- `diagnostic evidence`: what would reveal whether the problem is present;
- `repair`: a feasible model, design, measurement, or wording change;
- `surviving claim`: what remains defensible if the repair fails.

Rank issues by consequence. Do not turn the eight wedges into a mechanical checklist of requested appendices.

## Preserve evidence status

- AER `status: done` means the third-pass memory artifact was produced; it does not make every paper-level claim source-verified.
- The AEJ corpus is an OCR-derived second-pass card library, not strict completion proof for 107 papers.
- Reopen the relevant per-paper memory and source pack for substantive use.
- Locate a clean PDF or page image for exact equations, theorems, tables, figures, proofs, quotations, and layout claims.
- Label transferable cross-paper patterns as expert synthesis or inference.
