from datetime import datetime, timezone
import requests
from geopy.geocoders import Nominatim
import folium

API_KEY = "cb7139531260802c6ba40fb2ee5ffe24"  # replace with your real API key

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    today = datetime.now(timezone.utc)
    day = today.day
    month = today.month

    features = [
        day,
        month, 
        data["main"]["temp"],
        data["main"]["humidity"],
        data["wind"]["speed"],
        data.get("visibility", 10000) / 1000,
        0,
        data["main"]["pressure"]
    ]
    return features, data

def geocode_city(city):
    geolocator = Nominatim(user_agent="city_map_app")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None

def create_map(latitude, longitude, temperature):
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=15,
        popup=f"Temperature: {temperature} °C",
        color="red" if temperature > 25 else "blue",
        fill=True,
        fill_opacity=0.6
    ).add_to(m)
    return m
