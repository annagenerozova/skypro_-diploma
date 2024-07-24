from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://fstravel.com/searchtour")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()
  
    def tour_search (self):
        close_button = WebDriverWait(self._driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@class="popmechanic-close"]')))
        close_button.click()
        self._driver.find_element(By.CSS_SELECTOR, '[name="Город"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, '[name="Город"]').send_keys("Санкт-Петербург")
        self._driver.find_element(By.CSS_SELECTOR, '[placeholder="Страна, город, отель"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, '[placeholder="Страна, город, отель"]').send_keys("Турция")
        self._driver.find_element(By.CSS_SELECTOR, '[class="calendar__field-button"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="27"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '[class="v-nights__pinput"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '[class="v-tourists__pinput"]').click()
        self._driver.find_element(By.XPATH, '//*[@class="v-icon v-icon-plus_square active"]').click()
        self._driver.find_element(By.XPATH, '//*[@class="v-btn-yellow v-search-button"]').click()
    
    def get_departure_city(self):
        return self._driver.find_element(By.CSS_SELECTOR, '[name="Город"]').get_attribute('value')

    def like_tour(self):
        WebDriverWait(self._driver, 40).until(EC.element_to_be_clickable( (By.XPATH, '//*[contains(@class, "ui-icon-heart-container") and contains(@class, "hotel-card__img-favorites")]'))).click()
        self._driver.find_element(By.CSS_SELECTOR, "#v-favorite").click()
        added_to_favorites = self._driver.find_element(
                By.XPATH, '//*[contains(@class, "v-favorite-item v-mb-4 v-ml-2 v-mr-2")]')
        assert added_to_favorites is not None, "Тур не добавлен в избранное"

    def choice_tour(self):
        original_window = self._driver.current_window_handle
        WebDriverWait(self._driver, 40).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".hotel-card__about.flex.line-height"))).click()
        new_window = [window for window in self._driver.window_handles if window != original_window][0]
        self._driver.switch_to.window(new_window)
        WebDriverWait(self._driver, 40).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="hotel__hotels-item__btn-text"]'))).click()
        self._driver.find_element(By.CSS_SELECTOR, "#v-basket").click()
        added_to_basket = self._driver.find_element(
                By.XPATH, '//*[contains(@class, "hotel-cart")]')
        assert added_to_basket is not None, "Тур не добавлен в корзину"
        
    def comparison_tour(self):
        buttons = WebDriverWait(self._driver, 40).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#compareIcon")))
        counter = 0
        for btn in buttons:
            btn.click()
            counter += 1

        self._driver.find_element(By.CSS_SELECTOR, '[class="account__compare"]').click()
        added_to_scales = self._driver.find_element(
                By.XPATH, '//*[contains(@class, "v-slider__body")]')
        assert added_to_scales is not None, "Туры не добавлены для сравнения"

    def delete_comparison(self):
       original_window = self._driver.current_window_handle
       WebDriverWait(self._driver, 30).until(
            lambda d: len(d.window_handles) > 1)
    #    WebDriverWait(self._driver, 30).until(EC.new_window_is_opened)
       new_window = [window for window in self._driver.window_handles if window != original_window][0]
       self._driver.switch_to.window(new_window)
       close_button = WebDriverWait(self._driver, 30).until(
              EC.element_to_be_clickable((By.XPATH, '//*[@class="close"]'))).click()
       WebDriverWait(self._driver, 40).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.slider__delete-block'))).click()# Проверка что тур удален
    #    WebDriverWait(self._driver, 30).until(
    #          EC.invisibility_of_element_located((By.CSS_SELECTOR, '.slider__delete-block')))
