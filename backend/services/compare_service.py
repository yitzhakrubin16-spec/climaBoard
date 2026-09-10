from schemas.compare import CompareCities
from services.weather_service import get_current_weather

def compare_cities_service(data: CompareCities):
    first_city_weather = get_current_weather(data.longitude_first, data.latitude_first)
    second_city_weather = get_current_weather(data.longitude_second, data.latitude_second)
    return {
        "first": first_city_weather, 
        "second": second_city_weather
        }