import requests

def get_weather(city):
    """Отримує погоду через API"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true"
    res = requests.get(url)
    if res.status_code != 200:
        raise ConnectionError("Не вдалося отримати дані")
    return res.json()
