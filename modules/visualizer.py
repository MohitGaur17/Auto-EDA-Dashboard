import plotly.express as px

def plot_histogram(df, column):
    fig = px.histogram(df, x=column, nbins=30)
    return fig

def plot_box(df, column):
    fig = px.box(df, y=column)
    return fig

def plot_correlation(df):
    corr = df.select_dtypes(include="number").corr()
    fig = px.imshow(corr, text_auto=True)
    return fig
