import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import time

base_url = "https://promptloggingsystem-backend.onrender.com"

unique_users = []

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)


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

    proxy_url = base_url + "/proxy-api/dashboard?"
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
        data = json_data.get("data", [])

        if data:
            # Create a DataFrame from the 'data'
            df = pd.DataFrame(data)

            # Print the DataFrame
            print("DataFrame from API response:")
            return df
        else:
            return pd.DataFrame()
            print("No data found in the API response.")
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
    time_range = st.selectbox("Select Time Period", time_ranges, index=0, key="time")

    # Button group for environments
    environments = [
        "All",
        "production",
        "development",
        "testing",
    ]
    environment = st.selectbox("Select Environment", environments, index=0, key="env")

    # Button group for environments
    models = [
        "All",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-0125-preview",
        "gpt-3-5-turbo",
        "gpt-4",
    ]
    model = st.selectbox("Select Model", models, index=0, key="model")

    statuss = ["All", "failed", "successful"]
    status = st.selectbox("Select Status", statuss, index=0, key="status")

    users = ["All"] + unique_users
    user = st.selectbox("Select User", users, index=0, key="user")

    return time_range_dict[time_range], environment, model, status, user


# Main function for Streamlit app
def main():
    global table
    # Title for the app
    st.title("Prompt Logger")
    # Add buttons for filtering

    all_data = get_all_data()
    unique_users = list(all_data["User"].unique())

    with st.expander("Filters"):
        time_range, environment, model, status, user = filter_options(unique_users)
        df_filtered = get_filter_data(time_range, environment, model, status, user)

    if df_filtered.empty:
        st.write("No data found for the selected filters.")
        return
    df_filtered["Created_At"] = pd.to_datetime(
        df_filtered["Created_At"] / 1000, unit="s"
    )

    table = st.dataframe(df_filtered)



if __name__ == "__main__":
    main()
