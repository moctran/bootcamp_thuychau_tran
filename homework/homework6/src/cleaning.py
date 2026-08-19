def fill_missing_median(df, columns):
    """
    Fill missing values in selected columns with each column's median.
    """
    df = df.copy()

    for col in columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    return df


def drop_missing(df, threshold=0.5):
    """
    Drop rows where the proportion of missing values
    is greater than the threshold.
    """
    df = df.copy()

    # Minimum number of non-missing values required
    min_non_missing = int((1 - threshold) * df.shape[1])

    df = df.dropna(thresh=min_non_missing)

    return df


def normalize_data(df, columns):
    """
    Normalize selected columns using Min-Max normalization:
    x_normalized = (x - min) / (max - min)

    Values will be between 0 and 1.
    """
    df = df.copy()

    for col in columns:
        min_value = df[col].min()
        max_value = df[col].max()

        df[col] = (df[col] - min_value) / (max_value - min_value)

    return df