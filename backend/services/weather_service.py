import requests
from fastapi import HTTPException

def get_current_weather(longitude: float, latitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"longitude": longitude, "latitude": latitude, "current": "temperature_2m,weather_code,wind_speed_10m,apparent_temperature"}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Open-Meteo request timed out")
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=502, detail="Error")

    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"],
        "apparent_temperature": data["current"]["apparent_temperature"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "weather_code": data["current"]["weather_code"]       
    }

def get_forecast(longitude: float, latitude: float, days: int):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"longitude": longitude, "latitude": latitude, "daily": "temperature_2m_max,temperature_2m_min", "forecast_days": days}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Open-Meteo request timed out")
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=502, detail="Error")


    data = response.json()

    forecast = []
    for i in range(len(data["daily"]["time"])):
        forecast.append({
            "date": data["daily"]["time"][i], 
            "max": data["daily"]["temperature_2m_max"][i], 
            "min": data["daily"]["temperature_2m_min"][i]})

    return forecast
    