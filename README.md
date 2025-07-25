
# 🔍 Hydrological Time Series Regression App

An interactive Marimo notebook app for loading, merging, analyzing, and modeling hourly hydrological time-series data. Designed for water resource analysts, hydropower engineers, and environmental scientists.

---

## 📦 Features

- 📂 Multi-file loader: Merge multiple time series CSVs into a single hourly-aligned dataset.
- ❌ Missing value detector: Reports missing timestamps per parameter.
- 📊 Linear regression using statsmodels with summary statistics.
- 🧠 Polynomial regression (degree=2) using scikit-learn.
- 📈 Visualizations: Plots observed vs. predicted values over time.
- ✅ Marimo notebook: Editable, executable, and shareable like a Python-powered notebook — but lighter and Git-friendly.

---

## 📁 Input Files

These 3 files are required and already included in the project:

62.5.0-Vannføring-time-v1.csv  
62.17.0-Vannføring-time-v1.csv  
62.115.0-Vannstand-time-v1.csv

Each file should:
- Use `;` as delimiter  
- Contain 2 columns: timestamp and value  
- Use `,` as decimal separator (e.g., 1,23)  
- Use time format: YYYY-MM-DD HH:MM:SSZ

---

## 🚀 How to Use

1. Clone the repository

git clone https://github.com/Kavrelithito/hydro_regression_app.git
cd hydro_regression_app


2. Install dependencies

   pip install -r requirements.txt

3. Launch the app with Marimo

   marimo run hydro_regression_app.py

Tip: You can edit and re-run any cell interactively via the Marimo UI.

---

## 📂 File Structure

hydro-regression-app/  
├── hydro_regression_app.py        # Marimo notebook (main app)  
├── requirements.txt               # Python dependencies  
├── README.md                      # This file  
├── 62.5.0-Vannføring-time-v1.csv  # Input time series 1  
├── 62.17.0-Vannføring-time-v1.csv # Input time series 2  
├── 62.115.0-Vannstand-time-v1.csv # Input time series 3

---

## ✅ Requirements

- Python 3.8 or higher  
- Marimo ≥ 0.14.13  
- pandas  
- matplotlib  
- scikit-learn  
- statsmodels

Install them with:

pip install -r requirements.txt

---

## 🛠️ Customization

- Change file paths in the `files` list inside the notebook.  
- Choose predictors and targets easily by editing variable names in regression cells.  
- Add your own models — linear, tree-based, or LSTM — it’s a plain Python notebook!

---

## 📜 License

MIT License  
Feel free to use, modify, and share this project with attribution.

The hydrological data used here is provided through Sildre by NVE (Norwegian Water Resources and Energy Directorate) under the Norwegian License for Open Government Data (NLOD), compatible with Creative Commons Attribution 3.0 Norway (CC BY 3.0).

---

## 🤝 Contributions

Pull requests and feedback are welcome!  
If you use this app in research or operations, please consider citing or giving a ⭐ on GitHub.

---

## 👤 Author

Created by Netra Timalsina

---

## 📷 Screenshots (Optional)

Demo GIFs here to show your app in action.![Screenshot 2025-07-25 225434](https://github.com/user-attachments/assets/5bff125f-4d82-4e11-9d9f-5848ff520440)
![Screenshot 2025-07-25 225334](https://github.com/user-attachments/assets/21f618fc-259c-4ba5-9626-ec2ca6048e77)
![Screenshot 2025-07-25 225259](https://github.com/user-attachments/assets/13bb40c0-1ca0-4012-85c9-355468ded8fb)

