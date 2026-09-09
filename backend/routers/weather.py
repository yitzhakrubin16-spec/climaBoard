from fastapi import APIRouter
import requests


router = APIRouter(prefix="/weather")

@router.get("/current")
def current_weather(longitude :float, latitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"longitude": longitude, "latitude": latitude, "current": "temperature_2m,weather_code,wind_speed_10m,apparent_temperature"}

    response = requests.get(url, params=params)

    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"],
        "apparent_temperature": data["current"]["apparent_temperature"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "weather_code": data["current"]["weather_code"]       
    }

@router.get("/forecast")
def forecast_weather(longitude :float, latitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"longitude": longitude, "latitude": latitude, "daily": "temperature_2m_max,temperature_2m_min"}

    response = requests.get(url, params=params)

    data = response.json()

    forecast = []
    for i in range(len(data["daily"]["time"])):
        forecast.append({
            "date": data["daily"]["time"][i], 
            "max": data["daily"]["temperature_2m_max"][i], 
            "min": data["daily"]["temperature_2m_min"][i]})

    return forecast
    