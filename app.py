import streamlit as st
import pandas as pd

from modules.data_loader import load_data
from modules.profiler import profile_data
from modules.visualizer import plot_histogram, plot_box, plot_correlation
from modules.insights import numeric_insights, missing_value_insights
from modules.utils import get_column_types

st.set_page_config(page_title="Auto EDA Dashboard", layout="wide")
st.title("📊 Automated Exploratory Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Dataset Overview")
    st.write(df.head())

    profile = profile_data(df)
    st.metric("Rows", profile["rows"])
    st.metric("Columns", profile["columns"])
    st.write("Duplicate Rows:", profile["duplicates"])

    numeric_cols, categorical_cols = get_column_types(df)

    st.subheader("Visualizations")
    if numeric_cols:
        col = st.selectbox("Select Numeric Column", numeric_cols)
        st.plotly_chart(plot_histogram(df, col))
        st.plotly_chart(plot_box(df, col))

    if len(numeric_cols) >= 2:
        st.subheader("Correlation Heatmap")
        st.plotly_chart(plot_correlation(df))

    st.subheader("Automated Insights")
    for insight in numeric_insights(df):
        st.write("•", insight)
    for insight in missing_value_insights(df):
        st.write("•", insight)
