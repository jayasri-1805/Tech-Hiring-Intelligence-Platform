from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =========================================================
# THIP — Tech Hiring Intelligence Platform
# =========================================================

st.set_page_config(
    page_title="THIP | Hiring Intelligence",
    page_icon="T",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# STYLING — KEEP ALL CSS INSIDE THIS STRING
# =========================================================

st.markdown(
    """
    <style>
    :root {
        --ink: #172B4D;
        --muted: #52647D;
        --line: #DCE3ED;
        --canvas: #F4F6FA;
        --blue: #4568A8;
        --teal: #25877F;
    }

    html, body, [class*="css"] {
        font-family: "Segoe UI", Arial, sans-serif !important;
    }

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background: var(--canvas) !important;
        color: var(--ink) !important;
    }

    [data-testid="stMain"] .block-container {
        max-width: 100% !important;
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 2rem clamp(1rem, 2.5vw, 2.5rem) 3rem !important;
        overflow-x: hidden !important;
    }

    [data-testid="stSidebar"] {
        background: #FFFFFF !important;
        border-right: 1px solid var(--line) !important;
    }

    [data-testid="stSidebar"] * {
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] label p {
        color: var(--ink) !important;
    }

    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stCaptionContainer"] p,
    [data-testid="stWidgetLabel"] p {
        color: var(--muted) !important;
        opacity: 1 !important;
    }

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        color: var(--ink) !important;
        opacity: 1 !important;
    }

    .brand {
        color: var(--ink) !important;
        font-size: 27px;
        font-weight: 750;
        letter-spacing: -0.8px;
    }

    .brand-caption {
        color: var(--muted) !important;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.4px;
        margin: 2px 0 24px;
    }

    .eyebrow {
        color: var(--blue) !important;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }

    .page-title {
        color: var(--ink) !important;
        font-size: clamp(27px, 3vw, 36px);
        font-weight: 700;
        line-height: 1.25;
        letter-spacing: -0.8px;
        margin: 0;
    }

    .page-subtitle {
        color: var(--muted) !important;
        font-size: 14px;
        line-height: 1.6;
        margin: 9px 0 24px;
    }

    .section-title {
        color: var(--ink) !important;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 3px;
    }

    .section-caption {
        color: var(--muted) !important;
        font-size: 13px;
        line-height: 1.5;
        margin-bottom: 12px;
    }

    [data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid var(--line) !important;
        border-radius: 9px !important;
        padding: 16px 18px !important;
        min-width: 0 !important;
        box-shadow: none !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] p {
        color: var(--muted) !important;
        opacity: 1 !important;
        font-size: 13px !important;
    }

    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] div {
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
        font-size: clamp(21px, 2vw, 30px) !important;
        font-weight: 700 !important;
    }

    [data-testid="stSelectbox"] label,
    [data-testid="stMultiSelect"] label,
    [data-testid="stTextInput"] label {
        color: var(--ink) !important;
    }

    /* Closed dropdown */
    [data-baseweb="select"] > div {
        background: #FFFFFF !important;
        border-color: #C7D2E0 !important;
        border-radius: 7px !important;
    }

    [data-baseweb="select"] input,
    [data-baseweb="select"] [role="combobox"],
    [data-baseweb="select"] span {
        color: var(--ink) !important;
        -webkit-text-fill-color: var(--ink) !important;
        opacity: 1 !important;
    }

    [data-baseweb="select"] svg {
        fill: var(--muted) !important;
        color: var(--muted) !important;
    }

    /* Selected multi-select tags */
    [data-baseweb="tag"] {
        background: #E7EEF9 !important;
        border: 1px solid #C8D7EE !important;
    }

    [data-baseweb="tag"] span,
    [data-baseweb="tag"] svg {
        color: #24477F !important;
        fill: #24477F !important;
        -webkit-text-fill-color: #24477F !important;
    }

    /* Open dropdown popup — dark text on white */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    [data-baseweb="popover"] [role="listbox"],
    [data-baseweb="menu"] {
        background-color: #FFFFFF !important;
        color: #172B4D !important;
        opacity: 1 !important;
    }

    [data-baseweb="popover"] [role="option"],
    [data-baseweb="popover"] [role="option"] *,
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] li * {
        color: #172B4D !important;
        -webkit-text-fill-color: #172B4D !important;
        opacity: 1 !important;
    }

    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="menu"] li:hover {
        background-color: #EDF2FA !important;
    }

    [data-baseweb="popover"] [aria-selected="true"],
    [data-baseweb="popover"] [aria-selected="true"] * {
        color: #172B4D !important;
        -webkit-text-fill-color: #172B4D !important;
        background-color: #E7EEF9 !important;
    }

    [data-testid="stPlotlyChart"],
    [data-testid="stDataFrame"] {
        background: #FFFFFF !important;
        border: 1px solid var(--line) !important;
        border-radius: 9px !important;
        overflow: hidden !important;
        max-width: 100% !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 16px !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        min-width: 0 !important;
    }

    .stButton > button,
    .stDownloadButton > button {
        border-radius: 7px !important;
        border: 1px solid #C7D2E0 !important;
        color: var(--ink) !important;
        background: #FFFFFF !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        border-color: var(--blue) !important;
        color: var(--blue) !important;
        background: #F0F5FF !important;
    }

    .status-note {
        color: var(--muted) !important;
        border-top: 1px solid var(--line);
        padding-top: 14px;
        margin-top: 24px;
        font-size: 12px;
    }

    @media (max-width: 900px) {
        [data-testid="stMain"] .block-container {
            padding: 1.25rem 1rem 2rem !important;
        }

        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="column"] {
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }
    }
    /* ==========================================
   THIP — UI POLISH
   ========================================== */

/* Consistent light application background */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #F4F6FA !important;
    color: #172B4D !important;
}

/* Remove Streamlit's automatic page navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Clean, light top toolbar */
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: #F4F6FA !important;
}

[data-testid="stHeader"] {
    border-bottom: 1px solid #E2E8F0 !important;
}

[data-testid="stHeader"] button,
[data-testid="stHeader"] svg {
    color: #334155 !important;
    fill: #334155 !important;
}

/* Hide the Deploy control for a cleaner local dashboard */
[data-testid="stAppDeployButton"] {
    display: none !important;
}

/* Sidebar spacing and typography */
[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid #DCE3ED !important;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0.65rem !important;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] label p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #263B59 !important;
    opacity: 1 !important;
}

/* Closed dropdown controls */
[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 1px solid #C7D2E0 !important;
    border-radius: 8px !important;
    min-height: 42px !important;
}

[data-baseweb="select"] input,
[data-baseweb="select"] [role="combobox"],
[data-baseweb="select"] [data-testid="stMarkdownContainer"],
[data-baseweb="select"] span {
    color: #172B4D !important;
    -webkit-text-fill-color: #172B4D !important;
    opacity: 1 !important;
}

/* Open dropdown: force a light popup and dark text */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] [role="listbox"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul {
    background: #FFFFFF !important;
    color: #172B4D !important;
    opacity: 1 !important;
}

[data-baseweb="popover"] [role="option"],
[data-baseweb="popover"] [role="option"] *,
[data-baseweb="menu"] li,
[data-baseweb="menu"] li * {
    background-color: transparent !important;
    color: #172B4D !important;
    -webkit-text-fill-color: #172B4D !important;
    opacity: 1 !important;
}

/* Hover and selected dropdown options */
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="menu"] li:hover {
    background: #EDF2FA !important;
    color: #172B4D !important;
}

[data-baseweb="popover"] [aria-selected="true"],
[data-baseweb="popover"] [aria-selected="true"] * {
    background: #E7EEF9 !important;
    color: #172B4D !important;
    -webkit-text-fill-color: #172B4D !important;
}

/* Selected filter chips */
[data-baseweb="tag"] {
    background: #E7EEF9 !important;
    border: 1px solid #C8D7EE !important;
}

[data-baseweb="tag"] *,
[data-baseweb="tag"] svg {
    color: #24477F !important;
    fill: #24477F !important;
    -webkit-text-fill-color: #24477F !important;
}

/* Dashboard cards */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #DCE3ED !important;
    border-radius: 10px !important;
    padding: 18px !important;
    box-shadow: 0 1px 2px rgba(23, 43, 77, 0.03) !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #52647D !important;
    opacity: 1 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #172B4D !important;
    -webkit-text-fill-color: #172B4D !important;
}

/* Chart containers */
[data-testid="stPlotlyChart"],
[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
    border: 1px solid #DCE3ED !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: #FFFFFF !important;
    color: #172B4D !important;
    border: 1px solid #C7D2E0 !important;
    border-radius: 8px !important;
    min-height: 40px !important;
    font-weight: 600 !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #EDF2FA !important;
    border-color: #4568A8 !important;
    color: #24477F !important;
}

/* Responsive layout */
@media (max-width: 900px) {
    [data-testid="stMain"] .block-container {
        padding: 1.25rem 1rem 2rem !important;
    }

    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        min-width: 100% !important;
    }
}
/* Hide Streamlit's developer toolbar menu */
[data-testid="stToolbarActions"],
[data-testid="stMainMenu"],
#MainMenu {
    display: none !important;
}

/* Keep the dashboard header clean */
[data-testid="stHeader"] {
    background: #F4F6FA !important;
    box-shadow: none !important;
    border-bottom: 1px solid #DCE3ED !important;
}
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# LOAD DATA
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "analytics" / "analytics_dataset.csv"


@st.cache_data
def load_data(path: str, modified_time: float):
    return pd.read_csv(path)
if not DATA_PATH.exists():
    st.error(f"Analytics dataset not found: {DATA_PATH}")
    st.stop()

try:
    df = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)
except Exception as exc:
    st.error(f"Could not load the analytics dataset: {exc}")
    st.stop()

try:
    df = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)
except Exception as exc:
    st.error(f"Could not load the analytics dataset: {exc}")
    st.stop()

if df.empty:
    st.warning("The analytics dataset contains no records.")
    st.stop()

required_columns = ["salary_midpoint", "is_remote"]
missing_columns = [column for column in required_columns if column not in df.columns]

if missing_columns:
    st.error("Missing required dataset columns: " + ", ".join(missing_columns))
    st.stop()

df["salary_midpoint"] = pd.to_numeric(
    df["salary_midpoint"], errors="coerce"
)
df["is_remote"] = pd.to_numeric(
    df["is_remote"], errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR AND FILTERS
# =========================================================

filter_columns = [
    ("country", "Country"),
    ("experience_bucket", "Experience level"),
    ("company_category", "Company category"),
    ("remote_category", "Work arrangement"),
    ("industry", "Industry"),
]

with st.sidebar:
    st.markdown('<div class="brand">THIP</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="brand-caption">HIRING INTELLIGENCE</div>',
        unsafe_allow_html=True,
    )

    st.caption("WORKSPACE")

    page = st.radio(
        "Navigation",
        ["Market overview", "Salary analysis", "Job records"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**FILTER DATA**")

    filtered = df.copy()

    for column, label in filter_columns:
        if column not in filtered.columns:
            continue

        options = sorted(
            filtered[column].dropna().astype(str).unique().tolist()
        )

        if not options:
            continue

        selected = st.multiselect(
            label,
            options=options,
            default=[],
            placeholder="All values",
            key=f"filter_{column}",
        )

        if selected:
            filtered = filtered[
                filtered[column].astype(str).isin(selected)
            ]

    st.divider()
    st.caption(f"{len(filtered):,} of {len(df):,} records shown")

    if st.button("Reset filters", use_container_width=True):
        for column, _ in filter_columns:
            st.session_state.pop(f"filter_{column}", None)
        st.rerun()

if filtered.empty:
    st.warning("No records match the selected filters. Reset or change filters.")
    st.stop()


# =========================================================
# HELPERS
# =========================================================

def section(title: str, caption: str = "") -> None:
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )
    if caption:
        st.markdown(
            f'<div class="section-caption">{caption}</div>',
            unsafe_allow_html=True,
        )


def style_chart(fig, height: int = 340):
    fig.update_layout(
        height=height,
        autosize=True,
        margin=dict(l=75, r=35, t=25, b=65),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Segoe UI, Arial, sans-serif",
            color="#334155",
            size=12,
        ),
        showlegend=False,
        hoverlabel=dict(
            bgcolor="#172B4D",
            font_color="#FFFFFF",
            font_size=13,
        ),
    )

    fig.update_xaxes(
        title_font=dict(color="#334155", size=12),
        tickfont=dict(color="#475569", size=11),
        showgrid=True,
        gridcolor="#E5EAF1",
        linecolor="#CBD5E1",
        zeroline=False,
        automargin=True,
    )

    fig.update_yaxes(
        title_font=dict(color="#334155", size=12),
        tickfont=dict(color="#475569", size=11),
        showgrid=False,
        linecolor="#CBD5E1",
        zeroline=False,
        automargin=True,
    )

    return fig


def salary_label(value) -> str:
    if pd.isna(value):
        return "N/A"
    return f"${value:,.0f}"


def show_chart(fig, height: int = 350) -> None:
    st.plotly_chart(
        style_chart(fig, height),
        use_container_width=True,
        config={"displaylogo": False, "responsive": True},
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="eyebrow">TECHNOLOGY LABOUR MARKET</div>',
    unsafe_allow_html=True,
)

page_copy = {
    "Market overview": (
        "Hiring market overview",
        "A data-led view of compensation, work arrangements and the technology hiring landscape.",
    ),
    "Salary analysis": (
        "Salary analysis",
        "Explore compensation distributions and compare salary patterns across the available dataset.",
    ),
    "Job records": (
        "Job records",
        "Inspect and filter the underlying analytics records.",
    ),
}

title, subtitle = page_copy[page]

st.markdown(
    f'<h1 class="page-title">{title}</h1>'
    f'<div class="page-subtitle">{subtitle}</div>',
    unsafe_allow_html=True,
)


# =========================================================
# KPI CARDS
# =========================================================

salary = filtered["salary_midpoint"].dropna()
remote_jobs = int(filtered["is_remote"].sum())
remote_share = (
    float(filtered["is_remote"].mean() * 100)
    if len(filtered)
    else 0.0
)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric("Job records", f"{len(filtered):,}")

with k2:
    st.metric(
        "Average salary",
        salary_label(salary.mean()) if not salary.empty else "N/A",
    )

with k3:
    st.metric(
        "Median salary",
        salary_label(salary.median()) if not salary.empty else "N/A",
    )

with k4:
    st.metric("Remote jobs", f"{remote_jobs:,}")

st.caption(
    f"Showing {len(filtered):,} records after filters. "
    f"Remote share: {remote_share:.1f}%."
)
st.write("")


# =========================================================
# MARKET OVERVIEW
# =========================================================

if page == "Market overview":
    left, right = st.columns([1.25, 1], gap="large")

    with left:
        section(
            "Salary distribution",
            "Frequency of salary midpoint values in the current selection.",
        )

        salary_data = filtered.loc[
            filtered["salary_midpoint"].notna(),
            ["salary_midpoint"],
        ]

        if salary_data.empty:
            st.info("No valid salary values are available for this selection.")
        else:
            fig = px.histogram(
                salary_data,
                x="salary_midpoint",
                nbins=28,
                labels={"salary_midpoint": "Salary midpoint (USD)"},
                color_discrete_sequence=["#4568A8"],
                opacity=0.92,
            )

            fig.update_traces(
                marker_line_width=0,
                hovertemplate=(
                    "Salary: $%{x:,.0f}<br>"
                    "Records: %{y:,}<extra></extra>"
                ),
            )

            show_chart(fig)

    with right:
        section(
            "Work arrangement",
            "Record count by remote status.",
        )

        remote_frame = pd.DataFrame(
            {
                "Work arrangement": ["Remote", "Not marked remote"],
                "Jobs": [
                    remote_jobs,
                    max(len(filtered) - remote_jobs, 0),
                ],
            }
        )

        fig = px.bar(
            remote_frame,
            x="Jobs",
            y="Work arrangement",
            orientation="h",
            text="Jobs",
            color_discrete_sequence=["#4568A8"],
        )

        fig.update_traces(
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{y}: %{x:,} jobs<extra></extra>",
        )

        fig.update_layout(
            xaxis_title="Job records",
            yaxis_title="",
        )

        show_chart(fig)

    st.write("")
    left, right = st.columns(2, gap="large")

    with left:
        section(
            "Countries with most records",
            "Top countries represented in the filtered dataset.",
        )

        if "country" in filtered.columns:
            counts = (
                filtered["country"]
                .dropna()
                .astype(str)
                .value_counts()
                .head(10)
                .rename_axis("Country")
                .reset_index(name="Job records")
            )

            if not counts.empty:
                fig = px.bar(
                    counts.sort_values("Job records"),
                    x="Job records",
                    y="Country",
                    orientation="h",
                    text="Job records",
                    color_discrete_sequence=["#4568A8"],
                )

                fig.update_traces(
                    textposition="outside",
                    cliponaxis=False,
                    hovertemplate="%{y}: %{x:,} records<extra></extra>",
                )

                show_chart(fig)
            else:
                st.info("Country values are unavailable.")
        else:
            st.info("The dataset has no country column.")

    with right:
        section(
            "Industry breakdown",
            "Industries with the most job records.",
        )

        if "industry" in filtered.columns:
            counts = (
                filtered["industry"]
                .dropna()
                .astype(str)
                .value_counts()
                .head(10)
                .rename_axis("Industry")
                .reset_index(name="Job records")
            )

            if not counts.empty:
                fig = px.bar(
                    counts.sort_values("Job records"),
                    x="Job records",
                    y="Industry",
                    orientation="h",
                    text="Job records",
                    color_discrete_sequence=["#25877F"],
                )

                fig.update_traces(
                    textposition="outside",
                    cliponaxis=False,
                    hovertemplate="%{y}: %{x:,} records<extra></extra>",
                )

                show_chart(fig)
            else:
                st.info("Industry values are unavailable.")
        else:
            st.info("The dataset has no industry column.")


# =========================================================
# SALARY ANALYSIS
# =========================================================

elif page == "Salary analysis":
    valid_salary = filtered.dropna(subset=["salary_midpoint"])

    if valid_salary.empty:
        st.info("No valid salary records match the current filters.")
    else:
        left, right = st.columns(2, gap="large")

        with left:
            section(
                "Salary distribution",
                "Salary midpoint frequency across the selected records.",
            )

            fig = px.histogram(
                valid_salary,
                x="salary_midpoint",
                nbins=35,
                color_discrete_sequence=["#4568A8"],
                labels={"salary_midpoint": "Salary midpoint (USD)"},
            )

            show_chart(fig)

        with right:
            grouping = next(
                (
                    column
                    for column in [
                        "experience_bucket",
                        "company_category",
                        "country",
                        "industry",
                    ]
                    if column in valid_salary.columns
                ),
                None,
            )

            group_label = (
                grouping.replace("_", " ").title()
                if grouping
                else "available category"
            )

            section(
                "Median salary comparison",
                f"Grouped by {group_label.lower()}.",
            )

            if grouping:
                comparison = (
                    valid_salary.groupby(
                        grouping,
                        dropna=True,
                    )["salary_midpoint"]
                    .median()
                    .sort_values(ascending=False)
                    .head(12)
                    .rename("Median salary")
                    .reset_index()
                )

                comparison[grouping] = comparison[grouping].astype(str)

                fig = px.bar(
                    comparison.sort_values("Median salary"),
                    x="Median salary",
                    y=grouping,
                    orientation="h",
                    color_discrete_sequence=["#25877F"],
                    labels={
                        "Median salary": "Median salary (USD)",
                        grouping: group_label,
                    },
                )

                fig.update_traces(
                    hovertemplate=(
                        "%{y}<br>"
                        "Median: $%{x:,.0f}<extra></extra>"
                    ),
                )

                show_chart(fig)
            else:
                st.info("No suitable grouping column is available.")

        st.write("")
        section(
            "Salary summary",
            "Descriptive statistics for the filtered salary records.",
        )

        summary = valid_salary["salary_midpoint"].describe()

        summary_df = pd.DataFrame(
            {
                "Statistic": [
                    "Count",
                    "Mean",
                    "Median",
                    "Standard deviation",
                    "Minimum",
                    "25th percentile",
                    "75th percentile",
                    "Maximum",
                ],
                "Value (USD)": [
                    f"{summary['count']:,.0f}",
                    f"${summary['mean']:,.2f}",
                    f"${summary['50%']:,.2f}",
                    (
                        f"${summary['std']:,.2f}"
                        if pd.notna(summary["std"])
                        else "N/A"
                    ),
                    f"${summary['min']:,.2f}",
                    f"${summary['25%']:,.2f}",
                    f"${summary['75%']:,.2f}",
                    f"${summary['max']:,.2f}",
                ],
            }
        )

        st.dataframe(
            summary_df,
            hide_index=True,
            use_container_width=True,
        )


# =========================================================
# JOB RECORDS
# =========================================================

else:
    section(
        "Analytics records",
        "Search and inspect records from the filtered dataset.",
    )

    search = st.text_input(
        "Search records",
        placeholder="Search across text fields...",
    )

    records = filtered.copy()

    if search.strip():
        text_columns = records.select_dtypes(
            include=["object", "string"]
        ).columns

        if len(text_columns):
            mask = (
                records[text_columns]
                .fillna("")
                .astype(str)
                .apply(
                    lambda column: column.str.contains(
                        search.strip(),
                        case=False,
                        regex=False,
                    )
                )
                .any(axis=1)
            )

            records = records[mask]

    st.caption(f"{len(records):,} matching records")

    st.dataframe(
        records,
        hide_index=True,
        use_container_width=True,
        height=480,
    )

    st.download_button(
        "Export filtered records as CSV",
        data=records.to_csv(index=False).encode("utf-8"),
        file_name="thip_filtered_records.csv",
        mime="text/csv",
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="status-note">
        THIP · Tech Hiring Intelligence Platform
        &nbsp;|&nbsp; Analytics generated from the project dataset.
        Figures reflect the current selection.
    </div>
    """,
    unsafe_allow_html=True,
)