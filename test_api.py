import requests
from TourApi import TourApi

api = TourApi("https://fstravel.com/searchtour")

#Поиск тура
def test_search_tour():
    city = "Санкт-Петербург"
    country = "Турция"
    start_date = "2024-08-01"
    nights_count = 7
    adults = 2
    body = api.search(city, country, start_date, nights_count, adults)
    assert body['status'] == 200
    assert "tours" in body
    assert isinstance(body["tours"], list)
    assert len(body["tours"]) > 0