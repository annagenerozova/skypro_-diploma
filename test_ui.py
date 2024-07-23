from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from UI.MainPage import MainPage

# Поиск тура
def test_search():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса SearchPage

    main_page.tour_search()
    browser.quit()
    
def test_like():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса SearchPage
    
    main_page.tour_search()
    main_page.like_tour()
    browser.quit()
    
def test_choice():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса SearchPage
    
    main_page.tour_search()
    main_page.choice_tour()
    browser.quit()
    
def test_comparison():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса SearchPage
    
    main_page.tour_search()
    main_page.comparison_tour()
    browser.quit()

def test_delete_comparison():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса SearchPage
    
    main_page.tour_search()
    main_page.comparison_tour()
    main_page.delete_comparison()

    browser.quit()