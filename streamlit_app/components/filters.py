import streamlit as st

def sidebar_filters(df):
    if "country" in df.columns:
        countries=["All"]+sorted(df["country"].dropna().unique().tolist())
        selected=st.sidebar.selectbox("Country",countries)
        if selected!="All":
            df=df[df["country"]==selected]
    return df
