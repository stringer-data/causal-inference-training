# 07 — Double Machine Learning: ACIC Challenge

## Method
Double/Debiased Machine Learning (DML) — Chernozhukov et al. (2018)

## Dataset
ACIC (Atlantic Causal Inference Conference) data challenge / IHDP semi-synthetic data

## Dataset Links
- ACIC challenge page: https://aciccomp.org/
- IHDP train data: https://www.fredjo.com/files/ihdp_npci_1-100.train.npz
- IHDP test data: https://www.fredjo.com/files/ihdp_npci_1-100.test.npz
- See `data/raw/SOURCE_NOTE.md` for download instructions.

## Research Question
Can Double Machine Learning recover treatment effects in settings with many confounders and flexible ML nuisance functions, outperforming naive OLS? The ACIC/IHDP benchmarks provide known ground-truth effects for evaluation.

## Identification Strategy
DML addresses the "regularization bias" that arises when using ML models directly in causal inference. The procedure uses cross-fitting (sample splitting) to orthogonalize treatment and outcome:

**Step 1 — Partial out confounders:**
```
Ỹ_i = Y_i - E[Y_i | X_i]        (residualized outcome)
D̃_i = D_i - E[D_i | X_i]        (residualized treatment)
```
Both expectations are estimated by ML models (e.g., gradient boosting, lasso).

**Step 2 — Estimate ATE:**
```
θ = (D̃'D̃)^{-1} D̃'Ỹ
```

Cross-fitting prevents overfitting bias from leaking from the nuisance estimation into the final estimator.

## Assumptions
1. **Unconfoundedness** — conditional on X, treatment is independent of potential outcomes.
2. **Overlap** — common support: `0 < P(D=1|X) < 1`.
3. **Regularity** — nuisance functions are well-approximated by the chosen ML models (Donsker or entropy conditions).
4. **Cross-fitting** — strict sample splitting prevents contamination.

## Planned Outputs
- [ ] Data loading and EDA (IHDP or ACIC)
- [ ] Naive OLS treatment effect (biased baseline)
- [ ] DML with lasso nuisance models (`doubleml`)
- [ ] DML with gradient boosting nuisance models (`econml`, `doubleml`)
- [ ] Comparison: OLS vs. DML point estimates and confidence intervals
- [ ] Evaluation against known ground truth (PEHE, bias, coverage)
- [ ] Cross-fitting illustration: why it matters

## Suggested Python Packages
- `doubleml` — DoubleML framework (PLR, PLIV, IRM, IIVM models)
- `econml` — LinearDML, CausalForestDML
- `scikit-learn` — lasso, gradient boosting nuisance learners
- `pandas` / `numpy` — data handling
- `matplotlib` — bias/coverage plots
