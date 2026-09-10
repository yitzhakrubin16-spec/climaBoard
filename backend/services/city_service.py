import requests

def search_city_service(name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": name}

    response = requests.get(url, params=params)

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
