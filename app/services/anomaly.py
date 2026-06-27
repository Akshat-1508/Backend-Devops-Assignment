def detect_anomalies(df):
    median = df["amount"].median()

    threshold = median * 3

    df["anomaly"] = "No"

    df.loc[
        df["amount"] > threshold,
        "anomaly"
    ] = "Yes"

    return df