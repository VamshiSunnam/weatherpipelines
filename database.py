import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="NYC Weather Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/weather_log.csv", parse_dates=['timestamp'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df.sort_values("timestamp")
    except Exception as e:
        st.error("Failed to load weather data.")
        return pd.DataFrame()

df = load_data()

st.title("📊 New York City Weather Dashboard")
st.markdown("Displaying historical weather data fetched from OpenWeatherMap API.")

# Summary Stats
if not df.empty:
    latest = df.iloc[-1]
    st.metric("🌡️ Temperature (°C)", latest["temperature"])
    st.metric("💧 Humidity (%)", latest["humidity"])
    st.metric("🌬️ Wind Speed (m/s)", latest["wind_speed"])
    st.write(f"Last updated: {latest['timestamp']} | Condition: {latest['description']}")

    # Charts
    st.subheader("📈 Temperature Trend")
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['temperature'], color='red', marker='o')
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Temperature Over Time")
    st.pyplot(fig)

    st.subheader("💧 Humidity Trend")
    fig2, ax2 = plt.subplots()
    ax2.plot(df['timestamp'], df['humidity'], color='blue', marker='x')
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Humidity (%)")
    ax2.set_title("Humidity Over Time")
    st.pyplot(fig2)
else:
    st.warning("No data to display yet.")
