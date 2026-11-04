
import streamlit as st
import pandas as pd
import sqlite3

# Page configuration
st.set_page_config(
    page_title="NextGen Learners – Internship Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 Internship Performance Dashboard")
st.caption("NextGen Learners | Data Science Internship Program")

# Database connection
conn = sqlite3.connect("nextgen.db")

applicants = pd.read_sql_query(
    "SELECT * FROM applicants", conn
)

interns = pd.read_sql_query(
    "SELECT * FROM interns", conn
)

scores = pd.read_sql_query(
    "SELECT * FROM hackathon_scores", conn
)

conn.close()

# Sidebar domain filter
st.sidebar.title("Dashboard Filters")
st.sidebar.markdown("---")
st.sidebar.caption("Project: Week 3")
st.sidebar.caption("Database: SQLite")
st.sidebar.caption("Dashboard: Streamlit")

domains = ["All"] + sorted(
    applicants["Domain Applied"].dropna().unique().tolist()
)

selected_domain = st.sidebar.selectbox(
    "Select Domain",
    domains
)

# Apply filter
if selected_domain == "All":
    filtered_applicants = applicants.copy()
    filtered_interns = interns.copy()
    filtered_scores = scores.copy()
else:
    filtered_applicants = applicants[
        applicants["Domain Applied"] == selected_domain
    ]

    filtered_interns = interns[
        interns["domain"] == selected_domain
    ]

    filtered_scores = scores[
        scores["domain"] == selected_domain
    ]

# KPI calculations
total_applicants = len(filtered_applicants)
total_interns = len(filtered_interns)

completed_interns = (
    filtered_interns["completion_status"] == "Completed"
).sum()

completion_rate = (
    completed_interns / total_interns * 100
    if total_interns > 0 else 0
)

# KPI display
st.subheader("Program Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Applicants", total_applicants)
col2.metric("Total Interns", total_interns)
col3.metric("Completed Interns", int(completed_interns))
col4.metric("Completion Rate", f"{completion_rate:.1f}%")

st.divider()

# Completion analysis
st.subheader("Intern Completion Analysis")

completion_data = (
    filtered_interns.groupby("completion_status")
    .size()
    .reset_index(name="Intern Count")
)

st.bar_chart(
    completion_data,
    x="completion_status",
    y="Intern Count"
)

# Average hackathon scores
st.subheader("Average Hackathon Score by Domain")

if not filtered_scores.empty:

    average_scores = (
        filtered_scores.groupby("domain")["score"]
        .mean()
        .round(2)
        .reset_index()
    )

    st.bar_chart(
    average_scores,
    x="domain",
    y="score",
    y_label="Average Score"
)

else:
    st.info("No hackathon scores available for this domain.")

st.divider()



# Top 10 Leaderboard
st.subheader("🏆 Top 10 Performers")

leaderboard = filtered_scores.merge(
    filtered_interns[
        ["intern_id", "applicant_id", "completion_status"]
    ],
    on="intern_id",
    how="left"
)

leaderboard = leaderboard.merge(
    applicants[["applicant_id", "Applicant Name"]],
    on="applicant_id",
    how="left"
)

leaderboard = leaderboard.sort_values(
    "score", ascending=False
).head(10)

st.dataframe(
    leaderboard[
        ["Applicant Name", "intern_id", "domain",
         "score", "completion_status"]
    ],
    use_container_width=True,
    hide_index=True
)


# Applicant conversion analysis
st.subheader("Applicant Conversion by Domain")

conversion_data = applicants.groupby(
    "Domain Applied"
).size().reset_index(name="Total Applicants")

completed_data = (
    interns[interns["completion_status"] == "Completed"]
    .groupby("domain")
    .size()
    .reset_index(name="Completed Interns")
)

conversion_data = conversion_data.merge(
    completed_data,
    left_on="Domain Applied",
    right_on="domain",
    how="left"
)

conversion_data["Completed Interns"] = (
    conversion_data["Completed Interns"].fillna(0)
)

conversion_data["Conversion Rate (%)"] = (
    conversion_data["Completed Interns"]
    / conversion_data["Total Applicants"] * 100
).round(2)

if selected_domain != "All":
    conversion_data = conversion_data[
        conversion_data["Domain Applied"] == selected_domain
    ]

st.dataframe(
    conversion_data[
        ["Domain Applied", "Total Applicants",
         "Completed Interns", "Conversion Rate (%)"]
    ],
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Note: Intern completion statuses and hackathon scores "
    "are simulated data for this project."
)

st.success("Dashboard loaded successfully!")
