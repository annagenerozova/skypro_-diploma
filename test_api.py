import requests
from TourApi import TourApi
import allure

api = TourApi("https://fstravel.com/searchtour")
api2=TourApi("https://fstravel.com/api")

@allure.id("SKYPRO-1")
@allure.epic("Тyр фирма Fun&Sun")
@allure.severity("blocker")
@allure.title("Поиск id города отправления ")
@allure.feature("ADD")
def test_id_city():
    with allure.step("поиск id"):
        city_name = "Санкт-Петербург"
        city_id = api2.get_city_id(city_name)
        print(f"The ID for {city_name} is {city_id}")

@allure.id("SKYPRO-2")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Поиск id страны прибытия")
@allure.feature("ADD")
#Поиск id страны пребывания
def test_id_country():
    with allure.step("поиск id"):
        country_name = "Турция"
        country_id = api2.get_coutry_id(country_name)
        print(f"The ID for {country_name} is {country_id}")

@allure.id("SKYPRO-3")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Поиск тура")
@allure.feature("ADD")
@allure.description("Запрос на поиск тура с заданными данными ")
def test_search_tour():
    with allure.step("Передача данных для поиска"):
        city_name = "Санкт-Петербург"
        city_id = api2.get_city_id(city_name) 
        country_name = "Турция"
        country_id = api2.get_coutry_id(country_name)
        city = city_id
        country = country_id
        start_date = "2024-08-01"
        nights_count = 7
        adults = 2
    with allure.step("Результаты запроса"):   
        result = api.search(city_id, country_id, start_date, nights_count, adults)
        if result:
            print(result)
        else:
            print("Failed to retrieve tour information.")

@allure.id("SKYPRO-4")
@allure.epic("Тyр фирма Fun&Sun")
@allure.severity("blocker")
@allure.title("Поиск id отеля")
@allure.feature("ADD")
@allure.description("Получение id отеля с переданными данными: страна отправления и страна прибытия")
def test_hotel_id():
    city_name = "Санкт-Петербург"
    city_id = api2.get_city_id(city_name) 
    country_name = "Турция"
    country_id = api2.get_coutry_id(country_name)
    hotel_ids =api2.post_hotel_ids(city_id,country_id)
    print("Hotel IDs:", hotel_ids)

@allure.id("SKYPRO-5")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Добавление тура в избранное")
@allure.feature("ADD")
@allure.description("Найти нужный отель/тур  и добавить его в избранное")
def test_like_tour():
    with allure.step("Передача данных для поиска"):
        city_name = "Санкт-Петербург"
        city_id = api2.get_city_id(city_name) 
        country_name = "Турция" 
        country_id = api2.get_coutry_id(country_name)
    with allure.step("Запрос на получение id отеля"):
        id_hotel=api2.post_hotel_ids(city_id, country_id)
    # понять почему не записывается в переменную id отеля
    with allure.step("Получение списка избранных"):
        body1_like =len(api2.list_like())
    with allure.step("Добавили отель в избранное"):
        hotel_like =api2.like(id_hotel)
    with allure.step("Получение списка избранных после добавления"):
        body2_like = len(api2.list_like())
    with allure.step("Сравнить размеры 2х списков"): 
        assert body2_like - body1_like == 1


@allure.id("SKYPRO-7")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Поиск тура по стране")
@allure.feature("ADD")
@allure.description("Переход по вкладке 'Поиск по странам' на главной странцие сайта - страна Тайланд ")
def test_thailand():
    result = api.thailand_tour  
    