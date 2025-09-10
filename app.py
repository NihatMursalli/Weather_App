import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from datetime import datetime, timezone, timedelta
from utils.weather import get_weather_data, geocode_city, create_map
from streamlit_folium import st_folium

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Weather App", page_icon="🌦️", layout="wide")

st.title("🌦️ Weather App")
city = st.text_input("Enter your city (e.g., Baku):")

if city:
    try:
        X, current_data = get_weather_data(city)
        prediction = model.predict([X])[0]

        # Weather statistics
        with st.container():
            st.markdown(f"""
                <div style="padding: 1rem; margin-bottom: 32px; margin-top: 16px; background-color: #1a1e2a; border-radius: 10px;">
                    <h4 style="color: white; text-align: center;">🌤️ Current Temperature in {city.title()}: {current_data["main"]["temp"]} °C</h4>
                    <h4 style="color: white; text-align: center;">🔮 Predicted Temperature for Tomorrow: {prediction:.2f} °C</h4>
                </div>
            """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center;">
                    <div style="text-align:center;">
                        <h5>💧 Humidity</h5>
                        <h3>{current_data['main']['humidity']} %</h3>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center;">
                    <div style="text-align:center;">
                        <h5>🌬️ Wind Speed</h5>
                        <h3>{current_data['wind']['speed']} m/s</h3>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        col3, col4 = st.columns(2)
        with col3:
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center;">
                    <div style="text-align:center;">
                        <h5>🌫️ Visibility</h5>
                        <h3>{current_data.get('visibility', 10000)/1000:.1f} km</h3>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center;">
                    <div style="text-align:center;">
                        <h5>📊 Pressure</h5>
                        <h3>{current_data['main']['pressure']} hPa</h3>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # 7-day forecast
        today = datetime.now(timezone.utc)
        days, temps = [], []

        for i in range(8):
            future_date = today + timedelta(days=i)
            day = future_date.day
            month = future_date.month

            features = [
                day,
                month,
                current_data["main"]["temp"],
                current_data["main"]["humidity"],
                current_data["wind"]["speed"],
                current_data.get("visibility", 10000) / 1000,
                0,  # rainfall placeholder
                current_data["main"]["pressure"]
            ]
            pred_temp = model.predict([features])[0]
            days.append(future_date.strftime("%a"))
            temps.append(pred_temp)

        forecast_df = pd.DataFrame({"Day": days, "Predicted Temp (°C)": temps})
        st.subheader("📈 7-Day Temperature Forecast")
        st.line_chart(forecast_df.set_index("Day"))

        # Map
        st.subheader("🌍 City Location")
        latitude, longitude = geocode_city(city)
        if latitude and longitude:
            map_obj = create_map(latitude, longitude,
                                current_data["main"]["temp"])
            st_folium(map_obj, width=1400, height=425)
        else:
            st.error("Could not locate the city on the map.")

    except Exception as e:
        st.error(f"Something went wrong: {e}")

# Hide Streamlit branding
hide_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDecoration {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)
