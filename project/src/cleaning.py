import pandas as pd


def fill_missing_median(df, columns):
    """
    Fill missing values in selected numeric columns
    using the median of each column.
    """
    df = df.copy()

    for col in columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    return df


def fill_missing_category(df, columns, value="UNKNOWN"):
    """
    Fill missing values in selected categorical columns
    with a specified placeholder.
    """
    df = df.copy()

    for col in columns:
        df[col] = df[col].fillna(value)

    return df


def drop_missing(df, threshold=0.5):
    """
    Drop rows where more than the specified proportion
    of columns are missing.

    Example:
        threshold=0.5 means rows with more than 50%
        missing values are removed.
    """
    df = df.copy()

    min_non_missing = int((1 - threshold) * df.shape[1])

    return df.dropna(thresh=min_non_missing)


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates().copy()


def remove_invalid_amounts(df):
    """
    Remove transactions with negative transaction amounts.

    Zero-value transactions are retained because they may
    still represent valid records in the source dataset.
    """
    df = df.copy()

    return df[df["amount"] >= 0].copy()


def normalize_data(df, columns):
    """
    Apply Min-Max normalization to selected numeric columns.

    Values are transformed to the range [0, 1].
    """
    df = df.copy()

    for col in columns:

        min_value = df[col].min()
        max_value = df[col].max()

        if max_value != min_value:
            df[col] = (
                (df[col] - min_value)
                / (max_value - min_value)
            )

    return df


def validate_transactions(df):
    """
    Perform basic validation checks on the transaction dataset.
    """

    required_columns = [
        "transaction_id",
        "step",
        "sender",
        "receiver",
        "amount",
        "type",
        "is_fraud"
    ]

    checks = {
        "required_columns_present": all(
            col in df.columns
            for col in required_columns
        ),

        "transaction_id_unique":
            df["transaction_id"].is_unique,

        "no_negative_amounts":
            (df["amount"] >= 0).all(),

        "sender_missing":
            df["sender"].isna().sum(),

        "receiver_missing":
            df["receiver"].isna().sum(),

        "amount_missing":
            df["amount"].isna().sum()
    }

    return checks


def preprocess_transactions(df):
    """
    Run the complete transaction preprocessing pipeline.

    The function:
    1. Removes highly incomplete rows.
    2. Fills missing transaction amounts with the median.
    3. Fills missing categorical identifiers.
    4. Removes duplicate records.
    5. Removes negative transaction amounts.
    """

    df = df.copy()

    # Remove heavily incomplete records
    df = drop_missing(df, threshold=0.5)

    # Numeric missing values
    df = fill_missing_median(
        df,
        ["amount"]
    )

    # Categorical missing values
    df = fill_missing_category(
        df,
        ["sender", "receiver", "type"]
    )

    # Remove duplicate records
    df = remove_duplicates(df)

    # Remove impossible transaction amounts
    df = remove_invalid_amounts(df)

    return df