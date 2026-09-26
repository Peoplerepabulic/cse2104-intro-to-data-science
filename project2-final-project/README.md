# Project 2 (Final) — Melbourne Housing Price Prediction

End-to-end regression project on the [Melbourne Housing Snapshot](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot)
dataset: EDA → baseline models → feature engineering → tuned models.

## Workflow

1. **EDA** — price distribution, price by property type (house / townhouse /
   unit), price vs. distance from CBD, price by room count, missing-value
   audit, correlation matrix.
2. **Baseline models** — Linear Regression, KNN, Decision Tree, Random Forest.
3. **Feature engineering** — missing-value handling, encodings, new features.
4. **Tuned models** — cross-validated hyperparameter tuning (e.g.
   `n_estimators` for Random Forest) on engineered features.

## Result

**Best model: Random Forest on engineered features — RMSE $265,222, R² = 0.823**,
explaining 82% of the variance in Melbourne house prices.

Model ranking (by RMSE):
Random Forest (engineered) > Random Forest (baseline) > Decision Tree > KNN >
Linear Regression

Notably, linear regression degrades badly after feature engineering (the
engineered feature space breaks its assumptions), while tree-based models keep
improving.

## Figures

| Figure | Description |
|---|---|
| figures/eda_overview.png | 6-panel EDA: price distribution, price by type/rooms, distance from CBD, missing values, correlations |
| figures/model_comparison.png | RMSE comparison: baseline models, engineered models, baseline vs. engineered |

## Layout

```
project2.ipynb          # Full analysis notebook (80 cells)
figures/                # Exported figures
```

## Data

Downloaded at runtime via `kagglehub` (`dansbecker/melbourne-housing-snapshot`,
`melb_data.csv`) — not committed to the repo.
