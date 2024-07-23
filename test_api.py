import requests
from TourApi import TourApi

api = TourApi("https://fstravel.com/searchtour")
api2=TourApi("https://fstravel.com/api")

#Поиск id города отправления
def test_id_city():
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name)
    print(f"The ID for {city_name} is {city_id}")

#Поиск id страны пребывания
def test_id_country():
    country_name = "Турция"
    country_id = api2.get_coutry_id(country_name)
    print(f"The ID for {country_name} is {country_id}")

# #Поиск тура
def test_search_tour():
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name) 
    country_name = "Турция"
    country_id = api2.get_coutry_id(country_name)
    city = city_id
    country = country_id
    start_date = "2024-08-01"
    nights_count = 7
    adults = 2

    result = api.search(city_id, country_id, start_date, nights_count, adults)
    if result:
        print(result)
    else:
        print("Failed to retrieve tour information.")

def test_hotel_id():
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name) 
    country_name = "Турция"
    country_id = api2.get_coutry_id(country_name)
    hotel_ids =api2.get_hotel_ids
    print("Hotel IDs:", hotel_ids)

# #Добавление тура в избранное
def test_like_tour():
    #нашли тур
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name) 
    country_name = "Турция" 
    country_id = api2.get_coutry_id(country_name)
    #Поиск id отеля
    id_hotel=api2.get_hotel_ids(city_id, country_id)
    #запросили список избранных
    body1_like =api2.list_like()
    #Добавили отель 
    hotel_like =api2.like(id_hotel)
    #запросили список после добавления 
    body2_like = api2.list_like()
    #Проверили разницу
    assert len(body1_like) + 1 == len(body2_like)

def test_delete_like_tour():
    #нашли тур
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name) 
    country_name = "Турция"
    country_id = api2.get_coutry_id(country_name)
    city = city_id
    country = country_id
    start_date = "2024-08-01"
    nights_count = 7
    adults = 2
    result = api.search(city_id, country_id, start_date, nights_count, adults)
    #Поиск id отеля
    id_hotel =api2.get_hotel_ids
    #добавление в избранное 
    body1_like =api2.like(id_hotel)
    #удаление из избранного
    body2_delete = api2.delete_like(body1_like)
   