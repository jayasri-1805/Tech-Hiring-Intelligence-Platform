import streamlit as st
from utils.api_client import health
import requests
import time

st.set_page_config(
    page_title="API Status",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ API Monitoring Dashboard")

st.markdown(
"""
Monitor the health of the FastAPI backend and Machine Learning model.
"""
)

st.divider()

start = time.time()

try:

    response = health()

    elapsed = round((time.time() - start) * 1000, 2)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🟢 API Online")

    with c2:
        if response["model_loaded"]:
            st.success("🤖 Model Loaded")
        else:
            st.error("❌ Model Missing")

    with c3:
        st.info(f"⚡ {elapsed} ms")

    st.divider()

    st.subheader("Connection Details")

    st.json(response)

except requests.exceptions.ConnectionError:

    st.error("❌ Cannot connect to FastAPI")

except Exception as e:

    st.error(str(e))

st.divider()

st.subheader("Server Information")

st.markdown("""
| Property | Value |
|----------|-------|
| Backend | FastAPI |
| ML Model | Scikit-Learn |
| API URL | http://127.0.0.1:8000 |
| Prediction Endpoint | /predict |
| Health Endpoint | /health |
| Dashboard | Streamlit |
""")

st.divider()

st.info(
"""
If the API is offline:

1. Open a terminal
2. Activate the virtual environment
3. Run:

```bash
python -m uvicorn app.api.main:app --reload
Then refresh this page.
"""
)