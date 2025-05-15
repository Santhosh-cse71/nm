import streamlit as st
from datetime import datetime

def prediction_system():
    st.title("AI-Powered Prediction System")
    st.write("Real-time disaster forecasting using advanced machine learning models (demo).")

    location = st.text_input("Location", placeholder="E.g., Coastal City, Mountain Valley")
    date = st.date_input("Date", value=datetime.today()) 

    if st.button("Generate Prediction"):
        if location:
            st.success(f"Generated mock prediction for {location} on {date.strftime('%Y-%m-%d')}")
            st.write("### Key Indicators (Mock Data)")
            st.write("- Current Flood Risk: Moderate")
            st.write("- 7-Day Earthquake Probability: Low (2.1%)")
            st.write("- Air Quality Index (AQI): Good (35)")
        else:
            st.error("Please enter a location.")    

def alert_system():
    st.title("Community-Centered Alert System")
    st.write("Timely, accessible, and actionable warnings for at-risk populations (demo).")

    if st.button("Send Test Alert"):
        st.info("Test Alert Sent! You've received a simulated emergency alert. Stay informed!")

    if st.button("Send CRITICAL Test Alert"):
        st.error("CRITICAL ALERT! This is a simulated CRITICAL emergency alert. Evacuate immediately!")

def data_management():
    st.title("Data Management & Sharing")
    st.write("Robust platform for collecting, processing, and securely sharing critical disaster-related data (demo).")

    uploaded_file = st.file_uploader("Upload data file (CSV, JSON, etc.)")
    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully.")
        # For demo, just show file details
        st.write("File details:")
        st.write(f"- Type: {uploaded_file.type}")
        st.write(f"- Size: {uploaded_file.size} bytes")

def community_hub():
    st.title("Community Preparedness Hub")
    st.write("Resources, training materials, and communication channels to empower at-risk populations (demo).")

    st.write("- Resource 1: Disaster Preparedness Guide")
    st.write("- Resource 2: Emergency Contact List")
    st.write("- Resource 3: Training Videos")
    st.write("Join the community forum and share your experiences!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Prediction System", "Alert System", "Data Management", "Community Hub"])

    if page == "Prediction System":
        prediction_system()
    elif page == "Alert System":
        alert_system()
    elif page == "Data Management":
        data_management()
    elif page == "Community Hub":
        community_hub()

if __name__ == "__main__":
    main()
