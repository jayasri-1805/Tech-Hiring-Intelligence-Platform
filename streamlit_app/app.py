
import streamlit as st

st.set_page_config(
    page_title="THIP | Hiring Intelligence",
    page_icon="T",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = {
    "WORKSPACE": [
        st.Page(
            "pages/0_Market_Overview.py",
            title="Market Overview",
            default=True,
        ),
        st.Page(
            "pages/3_Analytics.py",
            title="Analytics",
        ),
    ],
    "TOOLS": [
        st.Page(
            "pages/1_Predictions.py",
            title="Salary Prediction",
        ),
        st.Page(
            "pages/2_API_Status.py",
            title="API Status",
        ),
    ],
}

page = st.navigation(pages, position="sidebar")
page.run()
