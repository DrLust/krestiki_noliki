from selenium.webdriver.support.wait import WebDriverWait
from common_selenium import *
from elements import *


class polia_tasks():
    def __init__(self, driver):
        self.is_active = True
        self.is_complete = False
        self.driver = driver

    def start_task(self):
        if not self.is_active:
            return
        try:
            url = go(page_home)
            self.driver.implicitly_wait(4)
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            bt_poly_home = self.driver.find_element(By.CSS_SELECTOR, ".button.moscowpoly-home__button")
            bt_poly_home.click()
            bt_drop = self.driver.find_element(By.CLASS_NAME, 'button moscowpoly-drop-dices')
            bt_activate = self.driver.find_element(By.CLASS_NAME, 'button moscowpoly-info-button')
            if bt_activate.is_active:
                bt_activate.click()
            # click(self.driver, 'XPATH', "//div[@id='moscowpoly']/div/span[2]")
            # poly_main.click()
            i = 1
            while i < 3:
                self.driver.implicitly_wait(2)
                if bt_drop.is_active:
                    bt_drop.click()
                # click(self.driver, 'CSS', '.moscowpoly-drop-dices .c')
                # poly_drop.click()
                self.driver.implicitly_wait(10)
                if bt_activate.is_active:
                    bt_activate.click()
                # click(self.driver, 'CSS', 'button moscowpoly-info-button')
                self.driver.implicitly_wait(3)
                i += 1
            self.driver.find_element_by_css_selector('.moscowpoly-close').click()
        except Exception as e:
            print(e)
            return

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
