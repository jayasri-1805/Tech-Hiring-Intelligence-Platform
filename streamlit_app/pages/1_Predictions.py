import streamlit as st
from utils.api_client import predict

st.set_page_config(page_title="Salary Prediction", layout="wide")

st.title("🤖 AI Salary Prediction")

st.markdown(
"""
Enter job details below to estimate the expected salary using the trained
Machine Learning model.
"""
)

left, right = st.columns([2, 1])

with left:

    st.subheader("Job Information")

    job_title = st.text_input("Job Title", "Data Scientist")

    company_type = st.selectbox(
        "Company Type",
        [
            "Startup",
            "Product",
            "Service",
            "Enterprise"
        ]
    )

    industry = st.text_input(
        "Industry",
        "Technology"
    )

    country = st.text_input(
        "Country",
        "India"
    )

    city = st.text_input(
        "City",
        "Hyderabad"
    )

    remote_type = st.selectbox(
        "Remote Type",
        [
            "Remote",
            "Hybrid",
            "Onsite"
        ]
    )

    experience_level = st.selectbox(
        "Experience Level",
        [
            "Entry",
            "Mid",
            "Senior"
        ]
    )

    experience = st.slider(
        "Experience (Years)",
        0,
        20,
        3
    )

    employment_type = st.selectbox(
        "Employment Type",
        [
            "Full-time",
            "Contract",
            "Internship"
        ]
    )

with right:

    st.subheader("Company Details")

    company_size = st.selectbox(
        "Company Size",
        [
            "Small",
            "Medium",
            "Large"
        ]
    )

    company_category = st.selectbox(
        "Company Category",
        [
            "Growth",
            "Enterprise",
            "Startup"
        ]
    )

    job_market_phase = st.selectbox(
        "Market Phase",
        [
            "Expansion",
            "Stable",
            "Decline"
        ]
    )

    posted_year = st.number_input(
        "Posted Year",
        2020,
        2030,
        2025
    )

    years_since_posted = st.slider(
        "Years Since Posted",
        0,
        10,
        1
    )

    experience_bucket = st.selectbox(
        "Experience Bucket",
        [
            "0-2 Years",
            "3-5 Years",
            "6-10 Years",
            "10+ Years"
        ]
    )

    is_remote = 1 if remote_type == "Remote" else 0

    company_size_rank = {
        "Small": 1,
        "Medium": 2,
        "Large": 3
    }[company_size]

    remote_category = remote_type

    dataset_version = "v1"

st.divider()

if st.button("🚀 Predict Salary", use_container_width=True):

    payload = {

        "job_title": job_title,
        "company_type": company_type,
        "industry": industry,
        "country": country,
        "city": city,
        "remote_type": remote_type,
        "experience_level": experience_level,
        "min_experience_years": experience,
        "employment_type": employment_type,
        "posted_year": posted_year,
        "company_size": company_size,
        "experience_bucket": experience_bucket,
        "remote_category": remote_category,
        "is_remote": is_remote,
        "company_size_rank": company_size_rank,
        "company_category": company_category,
        "job_market_phase": job_market_phase,
        "years_since_posted": years_since_posted,
        "dataset_version": dataset_version,
    }

    try:

        response = predict(payload)

        salary = response["predicted_salary"]

        st.success("Prediction Successful")

        st.metric(
            "💰 Estimated Salary",
            f"${salary:,.2f}"
        )

        st.info(
            f"""
**Prediction Summary**

• Job Title: {job_title}

• Experience: {experience} Years

• Country: {country}

• Company Size: {company_size}

• Model: Linear Regression
"""
        )

    except Exception as e:

        st.error(f"Prediction Failed\n\n{e}")