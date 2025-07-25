import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import os
    import re
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
    import statsmodels.api as sm



    # List of input CSV files (adjust if needed)
    files = [
        "62.5.0-Vannføring-time-v1.csv",
        "62.17.0-Vannføring-time-v1.csv",
        "62.115.0-Vannstand-time-v1.csv"
    ]

    def heading_from_filename(file):
        """Extract variable name from filename (before '-time')."""
        base = os.path.basename(file)
        match = re.search(r'^(.*?)-time', base)
        return match.group(1) if match else base

    # Load base timeline from the first file
    col_time, col_val = pd.read_csv(files[0], sep=";", skiprows=1, nrows=0).columns[:2]
    df_base = pd.read_csv(files[0], sep=";", skiprows=1, usecols=[col_time, col_val])
    df_base[col_time] = pd.to_datetime(df_base[col_time], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")
    df_base[col_val] = df_base[col_val].str.replace(",", ".").astype(float)

    # Generate full hourly time range
    full_time = pd.DataFrame({
        col_time: pd.date_range(df_base[col_time].min(), df_base[col_time].max(), freq="1h")
    })

    # Merge first dataset into full timeline
    base_param = heading_from_filename(files[0])
    merged = pd.merge(full_time, df_base, on=col_time, how="left").rename(columns={col_val: base_param})

    # Loop over remaining files and merge them
    for file in files[1:]:
        param = heading_from_filename(file)
        col_time_curr, col_val_curr = pd.read_csv(file, sep=";", skiprows=1, nrows=0).columns[:2]
        df = pd.read_csv(file, sep=";", skiprows=1, usecols=[col_time_curr, col_val_curr])
        df[col_time_curr] = pd.to_datetime(df[col_time_curr], format="%Y-%m-%d %H:%M:%SZ", errors="coerce")
        df[col_val_curr] = df[col_val_curr].str.replace(",", ".").astype(float)

        df = pd.merge(full_time, df, left_on=col_time, right_on=col_time_curr, how="left")
        df = df.rename(columns={col_val_curr: param})
        df = df.drop(columns=[c for c in [col_time_curr] if c != col_time and c in df.columns])

        # Report missing timestamps
        missing = df[df[param].isna()]
        print(f"\nFile {param}: {len(missing)} missing timestamps.")
        if not missing.empty:
            print(missing[[col_time]])

        # Outer merge with the main merged DataFrame
        merged = merged.merge(df, on=col_time, how="outer")

    return LinearRegression, PolynomialFeatures, col_time, merged, plt, sm


@app.cell
def _(col_time, merged):
    # Select columns with only values (exclude time)
    value_columns = [col for col in merged.columns if col != col_time]

    # Extract only complete (non-missing) rows
    complete_rows = merged[merged[value_columns].notna().all(axis=1)]

    # Uncomment for debugging:
    # print(complete_rows)

    return


@app.cell
def _(merged, plt, sm):
    # Define predictors and target (adjust as needed)
    predictors = ['62.5.0-Vannføring', '62.17.0-Vannføring']
    target = '62.115.0-Vannstand'
    time_col = merged.columns[0]

    # Filter for rows with all selected data present
    df_sel = merged[[time_col] + predictors + [target]].dropna()

    X = df_sel[predictors]
    y = df_sel[target]

    # Fit OLS regression
    Xc = sm.add_constant(X)
    model = sm.OLS(y, Xc).fit()
    print(model.summary())

    # Plot observed vs. predicted values
    y_pred = model.predict(Xc)
    plt.figure(figsize=(8, 5))
    plt.plot(df_sel[time_col], y, 'o', label="Observed", alpha=0.6)
    plt.plot(df_sel[time_col], y_pred, 'r.', label="Predicted", alpha=0.7)
    plt.xlabel('Time')
    plt.ylabel(target)
    plt.title(f"Observed vs Predicted: {target}")
    plt.legend()
    plt.tight_layout()
    plt.show()

    return


@app.cell
def _(LinearRegression, PolynomialFeatures, merged, plt):


    def run_poly_regression_on_all(merged):
        """Run degree-2 polynomial regression for each target vs other variables."""
        time_col = merged.columns[0]
        param_cols = [col for col in merged.columns if col != time_col]

        for target in param_cols:
            predictors = [col for col in param_cols if col != target]
            df_sel = merged[[time_col] + predictors + [target]].dropna()
            if df_sel.empty:
                print(f"Skipping {target}: no complete data.")
                continue

            X = df_sel[predictors].values
            y = df_sel[target].values

            poly = PolynomialFeatures(degree=2, include_bias=False)
            X_poly = poly.fit_transform(X)

            model = LinearRegression().fit(X_poly, y)
            y_pred = model.predict(X_poly)

            print(f"\n🔁 Target: {target}, Predictors: {predictors}")
            print("R² score:", model.score(X_poly, y))
            print("Coefficients:", model.coef_)

            # Plot
            plt.figure(figsize=(8, 5))
            plt.plot(df_sel[time_col], y, 'o', label="Observed", alpha=0.6)
            plt.plot(df_sel[time_col], y_pred, 'r.', label="Predicted (Poly deg2)", alpha=0.7)
            plt.xlabel('Time')
            plt.ylabel(target)
            plt.title(f"Polynomial Regression (deg=2): {target}")
            plt.legend()
            plt.tight_layout()
            plt.show()

    # Run it
    run_poly_regression_on_all(merged)

    return


if __name__ == "__main__":
    app.run()
