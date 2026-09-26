# Project 1 (Midterm) — What Drives Life Expectancy Across U.S. Counties?

Exploratory data analysis of the **2024 County Health Rankings analytic data**
(3,195 counties × 770 columns), asking which socioeconomic and health factors
best explain county-level life expectancy.

## Key findings

- Median county life expectancy: **75.8 years**, roughly bell-shaped with a
  long left tail (Fig. 1).
- Median household income correlates strongly with life expectancy
  (**r ≈ 0.73**); rurality alone is a weak predictor (Fig. 2, 3).
- Premature death, poor/fair health, smoking, and physical inactivity form a
  tightly correlated cluster (Fig. 3).
- State medians range from ~72 (MS) to ~80 (RI) years (Fig. 4).
- A composite unhealthy-behavior index rises steadily from urban to rural
  counties (Fig. 5).
- Linear regression (5-fold CV): socioeconomic features alone reach
  **R² = 0.615** vs. **0.289** for healthcare-access features; combined
  **R² = 0.647** (Fig. 6).
- Education and income inequality interact: high-education / low-inequality
  counties live ~7 years longer than low-education / high-inequality ones
  (Fig. 7).

## Figures

| Figure | Description |
|---|---|
| fig1_life_expectancy_dist.png | Distribution of life expectancy + KDE, median marked |
| fig2_income_vs_life_expectancy.png | Income vs. life expectancy, colored by % rural, OLS trend |
| fig3_correlation_heatmap.png | Correlation matrix of 12 health & socioeconomic indicators |
| fig4_state_life_expectancy.png | Median county life expectancy by state |
| fig5_behavior_index_by_rurality.png | Composite unhealthy-behavior index by rurality quartile |
| fig6_r2_comparison.png | Predictive power: socioeconomic vs. healthcare access (R², 5-fold CV) |
| fig7_edu_ineq_heatmap.png | Life expectancy by education × income-inequality quartiles |

## Layout

```
project1.ipynb          # Main analysis notebook
util.py                 # Plot styling helpers
data/analytic_data2024_0_l2ji.csv   # 2024 CHR analytic data (3,195 × 770)
figures/                # Exported figures (fig1–fig7)
project_filebrowser.db  # Scratch SQLite db used during analysis
```

## Reproduce

```console
conda activate cse2107
jupyter notebook project1.ipynb
```

Data source: [County Health Rankings & Roadmaps](https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation)
(2024 CHR CSV Analytic Data).
