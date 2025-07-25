# 🔍 Hydrological Time Series Regression App

An interactive [Marimo](https://github.com/marimo-team/marimo) notebook app for loading, merging, analyzing, and modeling hourly hydrological time-series data. Designed for water resource analysts, hydropower engineers, and environmental scientists.

---

## 📦 Features

- 📂 **Multi-file loader**: Merge multiple time series CSVs into a single hourly-aligned dataset.
- ❌ **Missing value detector**: Reports missing timestamps per parameter.
- 📊 **Linear regression** using `statsmodels` with summary statistics.
- 🧠 **Polynomial regression (degree=2)** using `scikit-learn`.
- 📈 **Visualizations**: Plots observed vs. predicted values over time.
- ✅ **Marimo notebook**: Editable, executable, and shareable like a Python-powered notebook — but lighter and Git-friendly.

---

## 📁 Example Use Case

With the following hourly time series:

