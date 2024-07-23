import requests

class TourApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url

    def search(self,city, country , start_date, nights_count, adults):
        params = {
            "city": city,
            "country": country,
            "start_date": start_date,
            "nights_count": nights_count,
            "adults": adults
        }
        resp = requests.get(self.url , params=params)
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code} - {resp.text}")
        # Проверка содержания ответа
        try:
            return resp.json()
        except requests.exceptions.JSONDecodeError:
            raise Exception(f"Response is not JSON: {resp.text}")

