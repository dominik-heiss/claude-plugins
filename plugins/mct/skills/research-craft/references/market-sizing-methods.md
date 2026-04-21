# Market Sizing Methods — Reference

How to size a market credibly. Always use multiple methods and triangulate.

---

## Method 1: Top-Down

**Logic:** Start with the total addressable market (TAM) from published data, then apply filters to reach the relevant segment.

**Process:**
1. Find the total market size from a credible source (Tier 1 or 2)
2. Define your segmentation filters (geography, product category, customer type, price tier)
3. Apply each filter with a stated rationale and source
4. Arrive at the Serviceable Addressable Market (SAM) and Serviceable Obtainable Market (SOM)

**Example:**
```
Global EV market: EUR 500B (SRC001, 2024)
× European share: 22% (SRC002, Eurostat) = EUR 110B
× Charging infrastructure sub-segment: 15% of EV market (SRC003) = EUR 16.5B
× Addressable slice (DC fast-charging only): 40% (SRC004) = EUR 6.6B

Top-down estimate: ~EUR 6-7B for European DC fast-charging market
```

**Strengths:** Grounded in published data; easy to defend
**Weaknesses:** Depends on quality of the source and relevance of the segmentation; filters can compound error

---

## Method 2: Bottom-Up

**Logic:** Build from the unit level — count buyers × average spend, or transactions × average price.

**Process:**
1. Identify the unit of analysis (chargers installed, charging sessions, vehicles using chargers)
2. Find or estimate the count of units (government data, industry reports, extrapolation)
3. Estimate revenue per unit (price × utilization)
4. Multiply and check plausibility

**Example:**
```
EV fleet in Europe: 6M vehicles (SRC002, 2024)
× Average charging sessions/year using public chargers: 40 (industry estimate, SRC005)
× Average revenue per session: EUR 12 (SRC006, operator data)
= EUR 2.9B/year in charging revenue

Bottom-up estimate: ~EUR 3B for European public charging revenue
```

**Strengths:** Transparent; exposes assumptions; grounded in operational reality
**Weaknesses:** Requires reliable unit data; utilization assumptions are often uncertain

---

## Method 3: Analogy-Based

**Logic:** Compare to a similar, better-understood market and adjust for differences.

**Process:**
1. Identify a comparable market (similar structure, further advanced on an adoption curve)
2. Find the comparable market's size and penetration metrics
3. Adjust for differences (market size, regulatory environment, income level)
4. Extrapolate to your target market

**Example:**
```
US EV charging market: EUR 8B (SRC007, 2024), 15M EVs
European EV fleet: 6M vehicles → scale factor: 6/15 = 0.4
Adjusted for European pricing (~85% of US): EUR 8B × 0.4 × 0.85 = EUR 2.7B

Analogy estimate: ~EUR 2.5-3B
```

**Strengths:** Useful when direct data is sparse; can show where Europe is headed
**Weaknesses:** Structural differences may invalidate the analogy; always explain the adjustment factors

---

## Triangulation

Run all three methods (or at least two). If results converge: confidence is high.

| Method | Estimate | Confidence |
|--------|----------|-----------|
| Top-down | EUR 6-7B | Medium (filter assumptions uncertain) |
| Bottom-up | EUR 3B | Medium (utilization assumption is a proxy) |
| Analogy | EUR 2.5-3B | Low-medium (structural differences exist) |

**Divergence analysis:** Why do top-down and bottom-up differ? In this example: top-down includes hardware (charger equipment sales) while bottom-up counts only revenue per charging session. They measure different things — need to align definitions first.

**Working assumption:** Set a defensible number with explicit rationale. "Using EUR 3B as working assumption for public charging revenue, EUR 6-7B for total charging market including infrastructure. Source: bottom-up corroborated by analogy method."

---

## Sensitivity Analysis on Market Size

For financial models, show how market size uncertainty flows through to conclusions:

| Market Size Scenario | Assumption | Impact on Revenue Target |
|---------------------|-----------|--------------------------|
| Bear case | EUR 2B | Market too small for standalone play |
| Base case | EUR 3B | Market justifies entry with 15% share target |
| Bull case | EUR 7B | Significant upside if infrastructure market included |

This is more useful than debating which market size estimate is "correct."
