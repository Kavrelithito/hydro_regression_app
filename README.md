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

62.5.0-Vannføring-time-v1.csv
62.17.0-Vannføring-time-v1.csv
62.115.0-Vannstand-time-v1.csv


This app will:
- Align them on a common time axis  
- Detect missing values  
- Run regression models (linear and polynomial)  
- Plot and evaluate the performance of the models  

---

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/hydro-regression-app.git
cd hydro-regression-app

2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

3. Launch the app with Marimo
bash
Copy
Edit

hydro-regression-app/
├── hydro_regression_app.py    # Marimo notebook (main application)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── *.csv                      # Your input time series data files

marimo run hydro_regression_app.py

✅ Requirements
Python 3.8 or higher

Marimo ≥ 0.14.13

pandas

matplotlib

scikit-learn

statsmodels

Install with:

bash
Copy
Edit
pip install -r requirements.txt

🛠️ Customization
🔧 Change file paths in the files list inside the notebook.

🔄 Choose predictors and targets easily by editing variable names in regression cells.


📤 Add your own models — linear, tree-based, or LSTM — it’s a plain Python notebook!


📜 License
MIT License
Feel free to use, modify, and share this project with attribution.

🌊 The hydrological data provided through Sildre by NVE (Norwegian Water Resources and Energy Directorate) is licensed under the Norwegian License for Open Government Data (NLOD), which is compatible with Creative Commons Attribution 3.0 Norway (CC BY 3.0).

🤝 Contributions
Pull requests and feedback are welcome!
If you use this app in research or operations, please consider citing or giving a ⭐ on GitHub.

👤 Author
Created by [Your Name]
[YourWebsiteOrLinkedIn.com] (optional)

📷 Screenshots (Optional)
Coming soon — add screenshots or demo GIFs here to show your app in action.

yaml
Copy
Edit

---

✅ You can paste this **as-is** when creating or editing the `README.md` file in your GitHub repo. 
