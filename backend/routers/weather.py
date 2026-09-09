from fastapi import APIRouter
import requests


router = APIRouter(prefix="/weather")

@router.get("/current")
def current_weather(longitude :float, latitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"longitude": longitude, "latitude": latitude, "current": "temperature_2m,weather_code,wind_speed_10m,apparent_temperature"}

    response = requests.get(url, params=params)

    data = response.json()
    return data