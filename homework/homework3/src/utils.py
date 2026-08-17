import numpy as np

def get_summary_stats(df):
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.describe()