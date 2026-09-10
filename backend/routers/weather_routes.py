from fastapi import APIRouter, Query
from services.weather_service import get_current_weather, get_forecast
from schemas.weather import ForecastParams, CurrentWeatherParams
from typing import Annotated

router = APIRouter(prefix="/weather")

@router.get("/current")
def current_weather(params: Annotated[CurrentWeatherParams, Query()]):
    return get_current_weather(longitude=params.longitude, latitude=params.latitude)

@router.get("/forecast")
def forecast_weather(params: Annotated[ForecastParams, Query()]):
    forecast = get_forecast(longitude=params.longitude, latitude=params.latitude, days=params.days)
    return forecast
    