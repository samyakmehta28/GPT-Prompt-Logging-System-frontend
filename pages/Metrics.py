import streamlit as st
import time
import numpy as np
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Metrics", page_icon="📈")

base_url = "https://promptloggingsystem-backend.onrender.com"


def get_all_data():
    # API URL
    proxy_url = base_url + "/proxy-api/dashboard"
    # Make the GET request
    response = requests.get(proxy_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the JSON data
        json_data = response.json()

        # Extract the 'data' from the JSON
        data = json_data.get("data", [])

        if data:
            # Create a DataFrame from the 'data'
            df = pd.DataFrame(data)

            # Print the DataFrame
            print("DataFrame from API response:")
            return df
        else:
            print("No data found in the API response.")
    else:
        print("Failed to retrieve data from the API.")


def get_filter_data(time_range, environment, model, status, user):
    # API URL

    proxy_url = base_url + "/proxy-api/metric?"
    if time_range != "All":
        proxy_url += f"timePeriod={time_range}" + "&"
    if environment != "All":
        proxy_url += f"filters[Environment]={environment}" + "&"
    if model != "All":
        proxy_url += f"filters[Model]={model}" + "&"
    if status != "All":
        proxy_url += f"filters[Status]={status}" + "&"
    if user != "All":
        proxy_url += f"filters[User]={user}" + "&"

    proxy_url = proxy_url[:-1]

    # Make the GET request
    response = requests.get(proxy_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the JSON data
        json_data = response.json()

        # Extract the 'data' from the JSON
        data = json_data.get("data", []).get("data", [])
        total_input_tokens = json_data.get("Total_Input_Tokens", 0)
        total_output_tokens = json_data.get("Total_Output_Tokens", 0)
        print()

        # Create a DataFrame from the 'data'

        df = pd.DataFrame(data)
        # Print the DataFrame
        print("DataFrame from API response:")
        return df, total_input_tokens, total_output_tokens
    else:
        print("Failed to retrieve data from the API.")


def filter_options(unique_users):
    # Button group for time range
    time_range_dict = {
        "All": "All",
        "Last 5 minutes": "last5minutes",
        "Last 30 minutes": "last30minutes",
        "Last Hour": "last1hours",
        "Last 6 Hours": "last6hours",
        "Last Day": "last1days",
        "Last Week": "last7days",
        "Last 30 days": "last30days",
    }
    time_ranges = [
        "All",
        "Last 5 minutes",
        "Last 30 minutes",
        "Last Hour",
        "Last 6 Hours",
        "Last Day",
        "Last Week",
        "Last 30 days",
    ]
    time_range = st.sidebar.selectbox(
        "Select Time Period", time_ranges, index=0, key="time"
    )

    # Button group for environments
    environments = [
        "All",
        "production",
        "development",
        "testing",
    ]
    environment = st.sidebar.selectbox(
        "Select Environment", environments, index=0, key="env"
    )

    # Button group for environments
    models = [
        "All",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-0125-preview",
        "gpt-3-5-turbo",
        "gpt-4",
    ]
    model = st.sidebar.selectbox("Select Model", models, index=0, key="model")

    statuss = ["All", "failed", "successful"]
    status = st.sidebar.selectbox("Select Status", statuss, index=0, key="status")

    users = ["All"] + unique_users
    user = st.sidebar.selectbox("Select User", users, index=0, key="user")

    return time_range_dict[time_range], environment, model, status, user


all_data = get_all_data()
unique_users = list(all_data["User"].unique())

st.markdown("Metrics Dashboard")
st.sidebar.header("Filters")
time_range, environment, model, status, user = filter_options(unique_users)
df, total_input_tokens, total_output_tokens = get_filter_data(
    time_range, environment, model, status, user
)

if df.empty:
    st.write("No data found.")
    st.stop()

columns = st.columns(2)

columns[0].metric("Total Input Tokens", total_input_tokens)
columns[1].metric("Total Output Tokens", total_output_tokens)

# Convert Unix timestamp to datetime
df["Created_At"] = pd.to_datetime(df["Created_At"] / 1000, unit="s")

# Sort DataFrame by timestamp (if not already sorted)
df = df.sort_values("Created_At")

# Calculate Requests per Second (RPS)
rps_series = df["Created_At"].value_counts().sort_index().resample("1S").count()
rps_df = rps_series.to_frame(name="Requests per Second")

# Streamlit app
st.title("Requests per Second Plot")

# Line chart with Plotly
fig = px.line(
    rps_df,
    x=rps_df.index,
    y="Requests per Second",
    title="Requests per Second over Time",
)
fig.update_xaxes(title="Timestamp", tickformat="%m-%d %H:%M:%S")
fig.update_yaxes(title="Requests per Second")
st.plotly_chart(fig)
