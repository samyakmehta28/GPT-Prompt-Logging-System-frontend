import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import time

base_url = "https://promptloggingsystem-backend.onrender.com"


st.set_page_config(
    page_title="Prompt",
    page_icon="👋",
)



def post_query(model_type, prompt_text, user, env):
    proxy_url = base_url + "/proxy-api"
    # Define the request body
    payload = {
        "prompt": prompt_text,
        "metadata": {
            "user": user,
            "environment": env,
            "model": model_type,
        },
    }
    # Send POST request to the API
    response = requests.post(proxy_url, json=payload)

    # Check if request was successful (status code 200)
    if response.status_code == 201:
        # Extract the JSON data
        json_data = response.json()

        # Extract the 'data' from the JSON
        data = json_data.get("data", [])

        if data:
            # Create a DataFrame from the 'data'
            return data
        else:
            return "Failed to connect to the API"
    else:
        print("Error:", response.status_code, response.text)
        return "Failed to store in dataset"


def main():

    # Title for the app
    st.title("Response Generator")
    # Add buttons for filtering

    # Sidebar section for user input
    st.sidebar.header("Ask a Question")
    model_type = st.sidebar.selectbox(
        "Select Model Type",
        [
            "gpt-4-turbo-2024-04-09",
            "gpt-4-0125-preview",
            "gpt-3-5-turbo",
            "gpt-4",
        ],
    )

    env = st.sidebar.selectbox(
        "Select Environment",
        [
            "production",
            "development",
            "testing",
        ],
    )

    # Input field for prompt text
    username = st.sidebar.text_input("Enter User", "")
    prompt_text = st.sidebar.text_area("Enter Prompt Text", "")


    # Check if user clicked the "Get Data" button
    if st.sidebar.button("Generate Response"):
        # Query API and get data
        response = post_query(model_type, prompt_text, username, env)
        st.write(response)
        


if __name__ == "__main__":
    main()
