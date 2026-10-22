# Tech Hiring Intelligence Platform (THIP)

### Turning Technology Job-Market Data into Actionable Hiring Insights

THIP is a data analytics and machine learning project designed to explore technology hiring trends, salary patterns, experience requirements, and remote-work opportunities. It transforms job-market data into structured analytical datasets, interactive visualizations, and salary predictions through a unified platform.

---

## Overview

Understanding the technology job market requires more than browsing individual job postings. THIP processes job-market data and organizes it into meaningful indicators that help users explore compensation trends, hiring patterns, and workforce demand.

The platform combines data engineering, exploratory data analysis, business KPI computation, interactive dashboards, and machine learning-based salary prediction.

## Key Features

- **Data Processing Pipeline** — Ingests, cleans, validates, and transforms job-market data for analysis.
- **Feature Engineering** — Derives analytical features such as salary ranges, salary bands, experience categories, remote-work classifications, and company-size indicators.
- **Hiring Market Analytics** — Explores salary distributions, geographic trends, industry patterns, experience requirements, and remote-work opportunities.
- **Interactive Dashboard** — Uses Streamlit and Plotly to present job-market indicators and visual insights.
- **Salary Prediction** — Provides an interface for estimating salary using a machine learning model.
- **Prediction API** — Uses FastAPI to expose prediction and health-check endpoints.
- **Testing** — Includes automated tests for analytics and feature-engineering pipelines.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Data Visualization | Plotly |
| API | FastAPI |
| Data Exchange | CSV, JSON |
| Testing | Pytest |
| Version Control | Git, GitHub |

## Architecture

```text
                 Job-Market Dataset
                         |
                         v
                Data Ingestion
                         |
                         v
              Data Cleaning & Validation
                         |
                         v
                 Feature Engineering
                         |
                         v
              Analytics & KPI Engine
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Analytics Dataset       ML Prediction Model
             |                       |
             v                       v
      Streamlit Dashboard      FastAPI Backend
             |                       |
             v                       v
       Market Insights         Salary Estimates
```

## Project Structure

```text
THIP/
├── app/
│   └── api/
│       └── main.py
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── analytics/
├── models/
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── profiling/
│   ├── validation/
│   ├── feature_engineering/
│   ├── kpi_engine/
│   ├── analytics_pipeline/
│   └── warehouse/
├── streamlit_app/
│   ├── assets/
│   ├── components/
│   ├── pages/
│   └── utils/
├── tests/
├── templates/
├── warehouse/
├── main.py
├── train_model.py
├── requirements.txt
└── README.md
```

*The directory tree illustrates the project's intended organization; adjust it if your current repository differs.*

## Getting Started

### Prerequisites

- Python 3.10 or later, compatible with the project's dependencies
- Git
- A terminal or IDE such as Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/jayasri-1805/Tech-Hiring-Intelligence-Platform.git
cd Tech-Hiring-Intelligence-Platform
```

### 2. Create a Virtual Environment

**Windows — PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can run the project's Python executable directly instead.

### 3. Install Dependencies

If `requirements.txt` exists in the repository:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the Streamlit Dashboard

```bash
python -m streamlit run streamlit_app/app.py
```

Open the local URL displayed in the terminal, typically `http://localhost:8501`.

### 5. Start the Prediction API

Open a second terminal from the project root and activate the same virtual environment. Then run:

```bash
python -m uvicorn app.api.main:app --reload
```

If the backend module path or dependencies differ in your local version, use the actual API entry point configured in the repository.

When the API starts successfully, the interactive documentation is typically available at `http://127.0.0.1:8000/docs`.

## Analytical Capabilities

THIP's engineered features support analysis of:

- Salary distributions and salary bands
- Compensation patterns across industries and locations
- Experience-level requirements
- Remote, hybrid, and on-site work classifications
- Company-size and company-category patterns
- Job-posting recency and market indicators

The insights depend on the coverage, quality, and time range of the underlying dataset. Historical patterns should not automatically be interpreted as future hiring forecasts.

## Machine Learning

The project includes a model-training workflow and a salary-prediction interface.

The intended workflow is:

1. Prepare and validate the input data.
2. Engineer features for model training.
3. Train and evaluate candidate models.
4. Save the selected model artifact.
5. Serve predictions through the API.
6. Integrate predictions into the dashboard.

Prediction quality depends on the selected model, training data, feature compatibility, and evaluation results. Salary estimates are informational and should not be treated as guaranteed compensation offers.

## Testing

Run the available tests with:

```bash
python -m pytest tests/
```

A successful test run indicates that the tested components passed; it does not by itself validate every dashboard page or API workflow.

## Potential Use Cases

- **Students and Job Seekers:** Explore compensation patterns, experience requirements, and remote-work opportunities.
- **Recruiters and HR Teams:** Examine salary distributions and hiring patterns across job categories.
- **Analysts and Researchers:** Investigate relationships between job attributes and compensation.
- **Training and Placement Teams:** Use market insights to inform discussions about technology skills and career preparation.

These are potential applications of the platform, not claims of validated outcomes for every stakeholder.

## Future Enhancements

- Add time-series analysis of hiring demand.
- Introduce model evaluation metrics and prediction confidence information.
- Expand geographic and industry-level comparisons.
- Add automated data-quality and pipeline monitoring.
- Develop reproducible model-training and evaluation workflows.
- Improve API validation, error handling, and deployment documentation.

## Limitations

- Results depend on the availability and quality of the underlying job-market dataset.
- Correlation between job attributes and salary does not establish causation.
- Model predictions may be less reliable for underrepresented job categories or locations.
- Dataset licensing and redistribution permissions must be checked before publishing data.

