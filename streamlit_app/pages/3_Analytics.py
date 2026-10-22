import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

st.title("📊 Hiring Analytics Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/analytics/analytics_dataset.csv")

df = load_data()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Filters")

countries = ["All"] + sorted(df["country"].unique().tolist())
industries = ["All"] + sorted(df["industry"].unique().tolist())
experience = ["All"] + sorted(df["experience_level"].unique().tolist())

country = st.sidebar.selectbox(
    "Country",
    countries
)

industry = st.sidebar.selectbox(
    "Industry",
    industries
)

exp = st.sidebar.selectbox(
    "Experience Level",
    experience
)

filtered = df.copy()

if country != "All":
    filtered = filtered[
        filtered["country"] == country
    ]

if industry != "All":
    filtered = filtered[
        filtered["industry"] == industry
    ]

if exp != "All":
    filtered = filtered[
        filtered["experience_level"] == exp
    ]

# =========================================================
# KPI CARDS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Jobs",
    f"{len(filtered):,}"
)

c2.metric(
    "Average Salary",
    f"${filtered['salary_midpoint'].mean():,.0f}"
)

c3.metric(
    "Countries",
    filtered["country"].nunique()
)

c4.metric(
    "Industries",
    filtered["industry"].nunique()
)

st.divider()

# =========================================================
# ROW 1
# =========================================================

left, right = st.columns(2)

with left:

    fig = px.histogram(
        filtered,
        x="salary_midpoint",
        nbins=35,
        title="Salary Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    jobs = (
        filtered
        .groupby("country")
        .size()
        .reset_index(name="Jobs")
        .sort_values(
            "Jobs",
            ascending=False
        )
    )

    fig = px.bar(
        jobs,
        x="country",
        y="Jobs",
        title="Jobs by Country"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# ROW 2
# =========================================================

left, right = st.columns(2)

with left:

    exp_df = (
        filtered
        .groupby("experience_level")
        .size()
        .reset_index(name="Jobs")
    )

    fig = px.pie(
        exp_df,
        values="Jobs",
        names="experience_level",
        hole=.55,
        title="Experience Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    remote = (
        filtered
        .groupby("remote_category")
        .size()
        .reset_index(name="Jobs")
    )

    fig = px.bar(
        remote,
        x="remote_category",
        y="Jobs",
        title="Remote vs Hybrid vs Onsite"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# INDUSTRY
# =========================================================

industry_df = (
    filtered
    .groupby("industry")
    .size()
    .reset_index(name="Jobs")
    .sort_values(
        "Jobs",
        ascending=False
    )
)

fig = px.bar(
    industry_df,
    x="industry",
    y="Jobs",
    title="Industry Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered.head(25),
    use_container_width=True
)