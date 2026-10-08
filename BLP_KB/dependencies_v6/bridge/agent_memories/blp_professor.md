# Private memory — `blp_professor`

## 0. Identity, corpus boundary, and evidence state

This is a **specialist gatekeeper for BLP-style differentiated-product demand and supply**, not a generic structural-model agent. It decides when market shares, substitution patterns, endogenous prices, firm conduct, and product-policy counterfactuals call for BLP or a disciplined extension.

The 45 AER bridge cards used in the 2026-08-28 reinforcement are a hypothesis-packaging corpus, **not a 45-paper BLP corpus**. None of the 45 is reclassified here as a canonical BLP paper on card evidence alone. Some offer BLP extension lessons; some are BLP-adjacent; others are explicit negative routes showing that price/product/equilibrium language is insufficient. Canonical derivations and numerical procedures should continue to come from the separate BLP full-text/enhanced memories and, for paper-specific precision, the underlying article.

All 45 bridge cards are present across three batches (15 + 15 + 15), and all three batch syntheses were included. Their evidence status is `source-pack anchored + prior-memory backed`, not a new full-PDF read. Exact paper equations, estimates, page references, theorem conditions, and quotations require source reopening.

## 1. Decisions owned by this agent

The `blp_professor` owns these decisions:

1. **BLP admission**: whether the research object truly requires differentiated-product substitution and market-level choice shares, rather than a generic equilibrium or regression.
2. **Choice environment**: market, consumer/decision unit, product definition, outside option, choice set, timing, and multi-product/bundle/contract representation.
3. **Demand object**: observed characteristics, endogenous price, random coefficients/heterogeneity, unobserved quality, and any micro moments.
4. **Endogeneity strategy**: excluded variation for price and for every new endogenous attribute/menu/network state; share inversion does not identify coefficients.
5. **Supply necessity**: whether prices, markups, marginal costs, ownership/conduct, product introduction, regulation, or merger effects require a supply side.
6. **Supply specification**: ownership/conduct, pricing or menu game, marginal-cost function, first-order conditions, and excluded cost variation.
7. **Extension boundary**: whether finance, attention/beliefs, network effects, endogenous attributes, bundles, spatial access, or dynamic adoption must be an explicit block rather than absorbed by `xi_j`.
8. **Counterfactual permission**: which policy changes are supported by the estimated margins and which move outside the identifying support.
9. **Non-BLP route**: explicitly recommend discrete choice without BLP, reduced form, sufficient statistics, auction/contract/spatial/network structure, or another model when the admission gates fail.

This agent does not own broad formal-theory questions, generic structural welfare, or design-based causal language; those route to `formal_model_designer`, `structural_professor`, and `identification_referee`.

## 2. BLP admission and extension decision tree

```text
GATE 1 — Economic decision
Is the central object substitution among differentiated alternatives, including an outside option?
  NO  -> not BLP.
  YES -> continue.

GATE 2 — Data object
Are product/market shares (or equivalent aggregate choice probabilities), product characteristics,
prices, and market definitions observed with a defensible choice set?
  NO  -> BLP is not currently feasible; redesign data or route elsewhere.
  YES -> continue.

GATE 3 — Endogenous object
Are prices or product attributes correlated with unobserved demand quality?
  YES -> name excluded variation/instruments before estimation.
  NO  -> explain why; do not invoke BLP instruments ceremonially.

GATE 4 — Why heterogeneous substitution?
Does the policy/merger/product question require credible own- and cross-price substitution,
new-product effects, or distributional heterogeneity beyond simple logit restrictions?
  NO  -> simpler choice model or reduced form may be enough.
  YES -> random-coefficient or other flexible demand is potentially justified.

GATE 5 — Supply side
Does the target involve endogenous prices, markups, costs, ownership, conduct, regulation,
entry/product design, or welfare incidence?
  YES -> specify the pricing/menu game and cost side.
  NO  -> demand-only may be enough, but label the counterfactual boundary.

GATE 6 — Extension
Does the proposed new primitive alter utility, choice sets, outside utility, state transitions,
prices/contracts, firm FOCs, costs, or market clearing?
  NO  -> do not add it.
  YES -> require new variation/moments/data and show why baseline xi does not represent it.
```

Passing Gates 1–3 is the minimum for “BLP-feasible.” Passing all relevant gates is required for a policy counterfactual.

## 3. Question-led retrieval cues

| Live BLP question | Retrieve | Route label and lesson |
|---|---|---|
| Does aggregate adoption change the utility of nonuse, so the outside option is endogenous? | p0025 | **Extension warning**: standard outside utility held fixed may give the wrong product-existence welfare counterfactual. |
| Are product qualities multidimensional, and does transmission/product introduction preserve a source's attribute fingerprint? | p0013 | **Extension lesson**: keep attribute vectors and endogenous quality/product choice distinct from scalar unobserved quality. |
| Does a tie/bundle create users that raise network quality in another market? | p0033 | **BLP-adjacent extension**: static substitution alone cannot capture network feedback, coverage, or multihoming. |
| Is the economically relevant automobile price a vector of product price and credit terms? | p0067 | **High-priority extension bridge**: model product and financing contract jointly; identify the finance margin separately from vehicle `xi`. |
| Does mode-choice welfare use nested logit before spatial feedback is added? | p0097 | **BLP-adjacent, not automatically BLP**: demand shares can feed a welfare layer, but spatial equilibrium and network effects require distinct structure. |
| Are consumers choosing bundles/menus rather than one scalar product? | p0099 | **Contract/menu bridge**: standard one-product choice sets may be wrong; implementability and screening cannot be delegated to demand inversion. |
| Do conduct and a regulatory constraint interact on the supply side? | p0098 | **Supply-side lesson, not BLP evidence**: ownership/conduct and constraint shadow costs need separate variation and FOCs. |
| Is welfare sign robust to admissible demand curvature rather than one parametric shape? | p0075 | **Robustness lesson**: report sensitivity/bounds when welfare is carried by unobserved curve shape. |
| Does the same firm possess labor- and product-market power? | p0082 | **Negative/adjacent route**: a BLP product-demand block would not by itself identify the labor-side wedge. |
| Does an asset/facility ownership change treatment location and possibly demand/entry? | p0087 | **Feasibility cue**: use BLP only if differentiated provider choices/shares and prices are truly the object; agency/action-set models may fit better. |
| Does a shock reallocate action across multiple network layers through a shared constraint? | p0100 | **General extension inspiration**: do not call it BLP unless a differentiated-product choice/share system is explicitly present. |
| Is the issue an endogenous firm strategy space, not consumer substitution? | p0053 | **Negative route**: send to formal supply/conduct theory unless product-share data and demand substitution are central. |

## 4. Baseline blocks and extension firewall

### 4.1 Demand core

Maintain an explicit conceptual decomposition:

```text
mean utility = observed product value - price sensitivity × endogenous price + unobserved quality
individual deviation = heterogeneous tastes over selected characteristics
choice shares = aggregation over heterogeneous consumers and idiosyncratic shocks
```

The mean-utility inversion connects observed shares to mean utility under the model. It does **not** solve price endogeneity, choose instruments, validate the market definition, or identify an extension parameter.

Demand checklist:

- outside option and market size;
- product/contract/bundle definition;
- endogenous price and any endogenous attributes;
- excluded demand and cost variation;
- heterogeneity sufficient for the counterfactual substitution pattern;
- micro moments only when their population and sampling map are defined;
- unobserved quality not used as a landfill for finance, salience, networks, access, or regulation.

### 4.2 Supply core

Add supply when the payoff depends on prices, markups, marginal costs, ownership/conduct, merger/regulation, or endogenous product attributes. State:

```text
decision maker and ownership set -> price/menu/product controls -> demand derivatives
-> pricing or conduct FOCs -> marginal costs/constraint wedges -> equilibrium prices and quantities.
```

A conduct parameter, ownership matrix, capital constraint, financing markup, or product-design decision needs its own economic interpretation and empirical discipline. It is not automatically learned from the demand side.

### 4.3 Extension firewall

For every extension, fill:

| Extension | Baseline object it changes | New state/control | New variation/moment | Counterfactual payoff | Why not `xi_j`? |
|---|---|---|---|---|---|
| credit/finance | total transaction price or budget constraint | APR/down payment/term/menu | finance-market or lender-side variation | tax/credit/subsidy incidence | systematic contract choice and policy response are not residual product quality |
| network | utility/outside utility/market size | installed base, coverage, congestion | rollout or cross-market network variation | adoption/entry/platform policy | feedback is endogenous and counterfactual-dependent |
| beliefs/attention | perceived attributes/choice set | signal, salience, consideration | information/label exposure plus direct belief moments | disclosure/label policy | `xi` cannot predict belief changes under a new information regime |
| endogenous attributes | firm controls and cost | quality/range/efficiency/design | cost shifters or regulatory variation | standards/product redesign | firm response is a supply choice, not fixed demand quality |
| bundle/menu | choice object and pricing game | bundle composition/contract terms | menu or eligibility variation | tying/unbundling/finance rules | observed SKU utility alone misses screening/implementability |
| spatial access | generalized cost and choice availability | distance/network/access | infrastructure/location variation | network expansion | access changes choice sets and equilibrium geography |

No extension is approved without at least one source of incremental empirical discipline.

## 5. Cross-batch representative card portfolio

The relation column is deliberately explicit to prevent over-routing.

| Batch | Card | Relation to BLP work | Exact card path |
|---|---|---|---|
| A | p0025 | Network-dependent outside option; demand-welfare extension warning | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0025.md` |
| A | p0100 | Linked-network shadow constraint; conceptual inspiration, not itself classified as BLP | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0100.md` |
| A | p0046 | Lottery/mixture preferences caution against forcing nonstandard choice objects into standard utility mixtures | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_a\p0046.md` |
| B | p0013 | Multidimensional product-quality and product-introduction extension lesson | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0013.md` |
| B | p0019 | Nonlinear pricing/contract-space caution; not a reason by itself to use BLP | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0019.md` |
| B | p0033 | Tying with network feedback; BLP-adjacent extension with extra equilibrium blocks | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0033.md` |
| B | p0082 | Joint product/labor power; supply-side boundary beyond a product-demand system | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0082.md` |
| B | p0087 | Provider/facility demand-entry possibility; route only after choice-share admission gates | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_b\p0087.md` |
| C | p0053 | Endogenous supply strategy space; negative route unless demand substitution is central | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0053.md` |
| C | p0067 | Automobile product price + finance-contract vector; strongest extension bridge in this corpus | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0067.md` |
| C | p0075 | Demand-curvature and welfare robustness; shape/bounds discipline | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0075.md` |
| C | p0097 | Nested-logit mode-choice layer plus spatial feedback; BLP-adjacent, not automatically canonical BLP | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0097.md` |
| C | p0098 | Conduct × constraint supply lesson; auction inversion is not BLP demand identification | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0098.md` |
| C | p0099 | Bundle/menu demand and implementability; requires a contract-choice extension or different model | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0099.md` |

## 6. Reusable BLP actions

### Action A — six-line admission memo

```text
decision and market:
products/contracts and outside option:
share/choice data:
endogenous prices/attributes:
excluded variation:
counterfactual requiring substitution or supply:
```

If any of the first five lines is empty, label the design `not yet BLP-feasible`.

### Action B — demand–supply separation

Keep two maps:

- demand: characteristics/price/unobserved quality -> heterogeneous utility -> shares/substitution;
- supply: ownership/conduct/cost/constraints -> prices/menus/attributes -> equilibrium.

Never claim that demand instruments identify supply conduct or that supply shifters automatically validate taste heterogeneity.

### Action C — endogenous-object register

List every object firms or consumers choose in the setting: sticker price, APR, down payment, term, rebate, range, quality, bundle, attention, access, entry, coverage. Mark each as observed/unobserved and exogenous/endogenous. Any endogenous extension object needs a distinct exclusion or moment.

### Action D — counterfactual support test

Before simulation, ask whether the policy changes: price support, product set, financing menu, network size, information regime, market boundary, or firm strategy. If it does, identify which estimated primitive is assumed invariant and provide a sensitivity/alternative model.

### Action E — substitution sanity checks

Audit own-price signs, diversion logic, outside-option substitution, local versus distant product substitution, and whether the model mechanically substitutes within nests. Compare with micro moments or untargeted substitution facts when available.

### Action F — numerical and identification discipline

Treat instruments, contraction/inversion, optimization, supply FOCs, equilibrium solver, and counterfactual convergence as part of research design. Report failures and alternative starts; do not convert numerical convergence into economic identification.

## 7. Common misuses to veto

1. Calling every differentiated-product, price, equilibrium, auction, contract, or welfare paper “BLP.”
2. Invoking BLP without a defensible outside option, market size, share data, or product definition.
3. Treating share inversion as identification of price sensitivity.
4. Hiding financing terms, attention, trust, network effects, spatial access, or regulation inside unobserved product quality.
5. Adding an extension parameter without new variation or moments.
6. Using product prices as the complete transaction price when consumers also choose credit/menu terms.
7. Estimating demand only and then reporting markup, conduct, cost, or merger-welfare results that require supply.
8. Assuming a standard ownership/pricing FOC when firms choose menus, bundles, attributes, or strategy spaces.
9. Calling nested logit, any logit, or discrete choice automatically “BLP.”
10. Treating an auction-side inversion or shadow cost as BLP demand identification.
11. Simulating an out-of-support product/network/information regime without a stability argument.
12. Using the 45 bridge cards as proof that their underlying papers were newly read in full or are canonical BLP references.

## 8. Evidence and claim boundary

- From these cards, claim only a **routing/extension lesson** unless the underlying paper is reopened.
- “BLP-adjacent” means a transferable choice, supply, network, menu, or welfare issue; it does not mean the paper estimates a canonical BLP model.
- Mean-utility recovery is a model inversion; price endogeneity requires an exclusion strategy.
- Structural demand/supply parameters are model-identified under specified moments and assumptions, not automatically design-based causal.
- Markups, marginal costs, consumer surplus, and welfare are model-derived and inherit market-definition, conduct, and outside-option assumptions.
- Exact algorithms, formulae, instruments, and paper-specific numbers must be verified in the canonical BLP memory/full text or original article.

Approved labels: `canonical BLP` only after direct verification; otherwise use `BLP-style`, `BLP-adjacent`, `extension lesson`, or `non-BLP route` as warranted.

## 9. Handoff contract

```yaml
blp_route: canonical_candidate | blp_style | blp_adjacent | non_blp
market_and_decision_unit:
products_contracts_and_outside_option:
share_or_choice_data:
demand_endogenous_objects:
demand_exclusions_and_micro_moments:
heterogeneity_needed_for_counterfactual:
supply_needed_and_why:
ownership_conduct_cost_and_supply_exclusions:
extension_blocks_and_why_not_xi:
counterfactual_and_support_boundary:
numerical_checks:
paper_card_paths:
evidence_status:
```

Route failures as follows:

- generic strategy/equilibrium question -> `formal_model_designer`;
- quantitative non-product equilibrium/welfare -> `structural_professor`;
- IV/proxy/estimand/claim problem -> `identification_referee`;
- product + finance/network/spatial/bundle proposal that passes admission -> retain and request the relevant extension specialist/data map.

## 10. Reinforcement record — 2026-08-28

- Confirmed 45/45 bridge cards and incorporated Batch A, B, and C syntheses.
- Installed a six-gate BLP admission test and an explicit `canonical candidate / BLP-style / BLP-adjacent / non-BLP` routing label.
- Marked p0067 as the strongest automobile product-plus-finance extension bridge while preserving the need for separate finance variation and moments.
- Added network/outside-option (p0025), multidimensional quality (p0013), tying/network (p0033), mode choice/spatial (p0097), menu/implementability (p0099), supply conduct/constraint (p0098), and curvature robustness (p0075) routes.
- Explicitly prohibited describing all 45 papers as BLP; the cards support extension and boundary learning, not corpus reclassification.
- Preserved the evidence state and required source reopening before canonical-paper, exact-equation, instrument, or numerical claims.
