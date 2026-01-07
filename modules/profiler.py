def profile_data(df):
    profile = {}
    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]
    profile["missing"] = df.isnull().sum()
    profile["duplicates"] = df.duplicated().sum()
    profile["dtypes"] = df.dtypes
    return profile
