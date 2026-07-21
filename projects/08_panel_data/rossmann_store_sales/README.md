# 08 — Panel Data: Rossmann Store Sales

## Method
Panel regression with entity (store) and time fixed effects. `Promo2`'s
staggered start dates also make this a natural second pass at the
staggered-adoption event-study machinery from `01_difference_in_differences/marijuana_policy`.

## Dataset
Daily sales for 1,115 Rossmann drug stores (Germany), 2013-01-01 to
2015-07-31. Real data released for the 2015 Kaggle "Rossmann Store Sales"
competition. See `data/raw/SOURCE_NOTE.md`.

## Research Question
Product-analyst framing: does running a promotion increase store sales, and
by how much, once we account for each store's baseline level and for
shared seasonal/day-of-week effects? Separately: for the 571 stores that
opted into the standing `Promo2` promotion at different points in time, is
there a dynamic effect around each store's own start date (an event
study), the way there was around each state's legalization year in the
marijuana case study?

## Identification Strategy
**Within-store panel FE (for `Promo`):** `Promo` switches on and off
day-to-day within the same store, so store fixed effects absorb
time-invariant store characteristics (location, size, assortment) and the
`Promo` coefficient is identified off within-store variation, conditional
on day-of-week/month/year fixed effects for shared seasonality.

**Staggered-cohort event study (for `Promo2`):** same logic as the
marijuana legalization case — different stores adopt at different
`Promo2SinceWeek`/`Promo2SinceYear` values, so this is a staggered
treatment-timing design with the same caveats about naive TWFE bias
(Goodman-Bacon) that showed up there. Complication specific to this
dataset: many `Promo2` cohorts started before the 2013 sales panel begins,
so they contribute no pre-period and can only serve as later comparison
points, not part of the event-time analysis.

## Assumptions
1. **No reverse causality in `Promo` timing** — promotions aren't scheduled
   in response to expected sales dips/spikes in a way correlated with the
   error term (plausible for a centrally-planned retail calendar, but
   worth checking).
2. **Parallel trends** for the `Promo2` staggered design — stores that
   opt into `Promo2` earlier vs. later would have trended similarly absent
   the promotion.
3. **No interference** — one store's promotion doesn't shift sales at
   other (nearby/competing) stores in the sample.

## Planned Outputs
- [ ] Load and merge `train.csv` + `store.csv`
- [ ] Panel FE regression: `Sales ~ Promo + C(Store) + C(DayOfWeek) + C(month)`
- [ ] Check `Promo2` cohort start-date distribution, restrict to cohorts
      with usable pre-period within the observed panel
- [ ] Staggered event-study on `Promo2` (naive TWFE, then Sun-Abraham/CS
      comparison, same as marijuana_policy)
- [ ] Discuss reverse-causality risk for `Promo` timing specifically
