import numpy as np

def numeric_insights(df):
    insights = []
    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        mean = df[col].mean()
        std = df[col].std()
        insights.append(
            f"{col}: Mean = {mean:.2f}, Std = {std:.2f}"
        )
    return insights

def missing_value_insights(df):
    insights = []
    missing = df.isnull().mean() * 100
    for col, percent in missing.items():
        if percent > 0:
            insights.append(
                f"{col} has {percent:.1f}% missing values"
            )
    return insights
