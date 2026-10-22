import streamlit as st

def show_kpis(df):
    st.metric("Rows",len(df))
    st.metric("Columns",len(df.columns))
    if "salary_midpoint" in df.columns:
        st.metric("Average Salary",round(df["salary_midpoint"].mean(),2))
