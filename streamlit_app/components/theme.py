import streamlit as st

def apply_theme():
    st.markdown(
        '''
        <style>
        .main {padding-top:1rem;}
        div[data-testid="stMetric"]{
            border:1px solid #ddd;
            padding:10px;
            border-radius:10px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
