from common_selenium import *
from elements import *
from selenium import webdriver
from selenium.webdriver.support.select import Select

class pvp_task():
    def __init__(self, driver):
        self.is_active = True
        self.is_complete = False
        self.driver = driver

    def start_task(self):
        url = go(page_alley)
        self.driver.get(url)
        self.driver.get(go(page_travel2))
        div_elements = self.driver.find_elements(By.TAG_NAME, "div")
        try:
            select_country = Select(get_by_id(self.driver, pvp_land_dropdown))
            if select_country is not None:
                select_country.select_by_index(1).click()
            self.driver.find_element(By.CLASS_NAME, "button").click()
        except Exception as e:
            print(e)
