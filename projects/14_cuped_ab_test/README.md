# 14 — CUPED: Variance Reduction in A/B Testing

## Method
CUPED — Controlled-experiment Using Pre-Experiment Data (Deng et al., 2013)

## Research Question
Can we recover a small, real treatment effect that a standard A/B test misses
(or requires a much larger sample to detect), by using pre-experiment data
to reduce variance?

## Setup
Synthetic e-commerce A/B test:
- 10,000 users randomly assigned 50/50 to control / treatment
- Pre-experiment metric: revenue in the 30 days before the experiment
- Post-experiment metric: revenue during the experiment period
- True treatment effect: +$2.00 per user (small lift)
- Pre/post revenue are correlated — the key ingredient CUPED exploits

## Treatment and Outcome
| Variable | Description |
|---|---|
| `treatment` | Binary assignment — 1 = saw new feature, 0 = control |
| `pre_revenue` | Revenue per user in the 30 days before the experiment |
| `post_revenue` | Revenue per user during the experiment (outcome) |

## How CUPED Works
Standard A/B test compares `mean(post_revenue | treatment) - mean(post_revenue | control)`.
The variance of this estimate is driven by user-level variation in revenue.

CUPED adjusts each user's outcome:

```
post_revenue_cuped = post_revenue - θ × (pre_revenue - mean(pre_revenue))
θ = Cov(post_revenue, pre_revenue) / Var(pre_revenue)
```

Since treatment is random, `E[post_revenue_cuped]` is unchanged — the ATT estimate
stays unbiased. But variance drops because the part of post_revenue that is
predictable from pre_revenue has been subtracted out.

## Key Insight
The variance reduction is:

```
Var_reduction = 1 - (1 - Corr(pre, post)²)
```

A pre/post correlation of 0.7 gives ~50% variance reduction — equivalent to
doubling your sample size for free.

## Planned Outputs
- [ ] Synthetic data generation and EDA
- [ ] Standard A/B test estimate (naive difference in means + CI)
- [ ] CUPED adjustment (θ estimation, adjusted outcome)
- [ ] CUPED ATT estimate + CI
- [ ] Side-by-side comparison: naive vs CUPED CI width
- [ ] Variance reduction as a function of pre/post correlation
