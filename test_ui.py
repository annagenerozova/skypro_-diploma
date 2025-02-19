from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from UI.MainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.id("SKYPRO-1")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Поиск тура")
@allure.feature("ADD")
@allure.description("Запрос на поиск тура с заданными данными ")
def test_search():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) 

    main_page.tour_search()
    departure_city = main_page.get_departure_city()
    assert departure_city == "Санкт-Петербург", f"Expected 'Санкт-Петербург' but got {departure_city}"
    browser.quit()
    
@allure.id("SKYPRO-2")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Добавление тура в избранное")
@allure.feature("ADD")
@allure.description("Найти нужный отель/тур  и добавить его в избранное")
def test_like():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) 
    
    main_page.tour_search()
    main_page.like_tour()
    browser.quit()

@allure.id("SKYPRO-3")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Добавление тура в корзину")
@allure.feature("ADD")
@allure.description("Найти нужный отель/тур  и добавить его в корзину")    
def test_choice():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) 
    
    main_page.tour_search()
    main_page.choice_tour()
    browser.quit()

@allure.id("SKYPRO-4")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Добавление тура в сранение")
@allure.feature("ADD")
@allure.description("Найти нужные туры и добавить их в сранения")       
def test_comparison():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) 
    
    main_page.tour_search()
    main_page.comparison_tour()
    browser.quit()

@allure.id("SKYPRO-5")
@allure.epic("Тyр фирма Fun&Sun") 
@allure.severity("blocker")
@allure.title("Проверка url")
@allure.feature("ADD")
@allure.description("Открыть главную страницу проверить URL")
def test_logo():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.logo()
    browser.quit()

# https://fstravel.com/storage/images/logo.svg