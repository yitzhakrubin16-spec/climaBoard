import requests
from fastapi import HTTPException

def search_city_service(name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": name}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Open-Meteo request timed out")
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=502, detail="Error")
        
    data = response.json()    

    results = data.get("results", [])

    cities = []

    for i in range (len(results)):
        region = None
        for j in range(1,5):
            admin_key = f"admin{j}"
            if(results[i].get(admin_key)):
                region = results[i][admin_key]
                break
        cities.append({
            "id": results[i]["id"],
            "name": results[i]["name"],
            "country": results[i]["country"],
            "region": region,
            "latitude": results[i]["latitude"],
            "longitude": results[i]["longitude"],
            "timezone": results[i]["timezone"],
        })
    
    return cities
