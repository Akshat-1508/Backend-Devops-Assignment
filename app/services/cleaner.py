import pandas as pd


REQUIRED_COLUMNS = [
    "transaction_id",
    "merchant",
    "amount",
    "currency",
    "status"
]


def clean_csv(file_path):
    df = pd.read_csv(file_path)

    missing = []

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing.append(column)

    if missing:
        raise Exception(
            f"Missing required columns: {missing}"
        )

    df = df.drop_duplicates()

    df["merchant"] = (
        df["merchant"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    df["currency"] = (
        df["currency"]
        .astype(str)
        .str.upper()
    )

    df["status"] = (
        df["status"]
        .astype(str)
        .str.title()
    )

    df["amount"] = (
        pd.to_numeric(
            df["amount"],
            errors="coerce"
        )
    )

    df = df.dropna(subset=["amount"])

    if "category" not in df.columns:
        df["category"] = "Unknown"

    df["category"] = df["category"].fillna("Unknown")

    return df