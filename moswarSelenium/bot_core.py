import logging
import re

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from character import *
from common_selenium import *
from elements import *
from polia_tasks import polia_tasks
from pvp_task import pvp_task
from undetected_chromedriver import Chrome, ChromeOptions
from selenium_stealth import stealth

class BotCore:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                webgl_renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)
        self.driver.get(MOSWAR_URL)
        self.driver.maximize_window()
        self.character = Character()
        self.wait = WebDriverWait(self.driver, 10)

    def run(self):  # запуск бота
        try:
            self.__login()
            #self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            self.__run_tasks()
        except NoSuchElementException as exception:
            logging.exception("An error occurred while finding an element: %s", exception)
        except TimeoutException as exception:
            logging.exception("An error occurred while waiting for an element: %s", exception)
        except Exception as exception:
            logging.exception("An unexpected error occurred while running the bot: %s", exception)
        finally:
            self.driver.quit()

    def __login(self):
        try:
            login = self.driver.find_element(By.XPATH, "//input[@id='login-email']")
            if login is not None:
                login.send_keys(self.character.email)

            pw = self.driver.find_element(By.XPATH, "//input[@id='login-password']")
            if pw is not None:
                pw.send_keys(self.character.password)

            self.driver.find_element(By.CSS_SELECTOR, "input[value='Войти']").click()
            #self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        except (NoSuchElementException, TimeoutException):
            logging.exception("An error occurred while finding or waiting for an element")
            raise

        except Exception:
            logging.exception("An error occurred while running the bot")
            raise

        finally:
            self.driver.quit()

    def __run_tasks(self):
        # Последовательно делаем дела
        try:
            # self._do_clan_beast()
            # self._do_tower()
            self.__do_moscowpoly()
        except Exception as e:
            logging.exception("An error occurred while running the bot: %s", e)

    def __do_clan_beast(self):
        # Сдаем изумруды
        # 1) Попробуем положить изумруды в клан
        # Wait for the page to load
        #self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        izum_count = self.driver.find_element(By.XPATH, "// span[contains(text(), 'в клан')]")
        if izum_count is None:
            return
        # Есть изумруды, сдадим их
        url = convert_relative_url(PAGE_CLAN_BEAST)
        self.driver.get(url)
        # Wait for the page to load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        # self.driver.find_element(By.LINK_TEXT, "Внести").click()
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='alert alert1'] button:nth-child(1)"))).click()

    def __do_tower(self):
        # Заходим в телевышку
        # Сформируем список полезных предметов
        useful_items = ('Термопаста', 'Полезный пельмень', 'Элемент случайной коллекции')
        useful_gold_items = ()
        # Переходим на https://www.moswar.ru/square/tvtower/
        url = convert_relative_url(PAGE_TOWER)
        self.driver.get(url)
        # Нахождение элемента кнопки по классу и атрибуту onclick
        #button = self.driver.find_element(By.CSS_SELECTOR, "div.action[onclick*='/square/tvtower/']")
        self.driver.implicitly_wait(10)
        # Нажатие на кнопку
        #button.click()
        self.driver.implicitly_wait(20)
        # Wait for the page to load
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'body')))
        # Проверим, сколько есть ещё попыток
        counter_element = get_by_class(self.driver, "tv-tower-news-today-counter")
        counter_text = counter_element.text
        # Извлекаем цифры из текста
        numbers = [int(s) for s in counter_text.split() if s.isdigit()]
        if numbers and len(numbers) > 0:
            counter = numbers[0]
            # Если попытки кончились, то выходим
            if counter == 5:
                return
        # Посмотрим, возможно ли улучшение
        tower_level_text = get_by_class(self.driver, "tv-tower-title-text").text
        numbers = re.findall(r'd+', tower_level_text)
        if len(numbers) > 0:
            tower_level = int(numbers[0])
            # Есть возможность для улучшения
            if tower_level < 15:
                self.__do_tower_upgrade()

        # Ищем все элементы с классом "tv-tower-news-text"
        news_elements = get_by_class(self.driver, "tv-tower-award")

        # Перебираем найденные элементы
        for element in news_elements:
            # Проверяем, содержит ли элемент нужный текст награды
            if element.text in useful_items:
                # Находим кнопку внутри элемента и нажимаем на нее
                button = element.find_element_by_xpath(
                    ".//following-sibling::div[@class='tv-tower-news-action']//div[contains(@class, 'button')]")
                if button:
                    self.driver.implicitly_wait(20)
                    button.click()

    def __do_tower_upgrade(self):
        # Закрыто на ремонт
        url = convert_relative_url(PAGE_TOWER)
        self.driver.get(url)

    def __do_moscowpoly(self):
        # Бросим кубики в Москвополии
        # Переходим в Хату
        button = self.driver.find_element(By.CSS_SELECTOR, "a.home[onclick*='AngryAjax.goToUrl']")
        if button:
            # Нажатие на кнопку
            button.click()
            # Ожидание загрузки страницы
            self.__wait_for_loading()
            # К Москвополии
            button = self.driver.find_element(By.XPATH,"//div[contains(@class, 'c') and contains(text(), 'К Москвополии')]")
            if button:
                #  Переходим на игровое поле
                button.click()
                WebDriverWait(self.driver, 5)
                for i in range(4):
                    button = self.driver.find_element(By.XPATH,
                    "//button[contains(@class, 'button moscowpoly-drop-dices')]//div[contains(@class, 'c') and contains(text(), 'Бросить кубик')]")
                    if button:
                        # Бросаем кубик
                        button.click()
                        # И ждем
                        WebDriverWait(self.driver, 15)
                        # Проверим, что выпала активная кнопка
                        button = self.driver.find_element(By.XPATH,
                        "//button[contains(@class, 'button moscowpoly-info-button')]//div[contains(text(), 'Активировать бонус')]")
                        if button:
                            # Активируем бонус
                            button.click()
                        # И ждем
                        WebDriverWait(self.driver, 5)

    def __do_pvp_task(self):
        # Кругосветка
        pass

    def __wait_for_loading(self):
        # Ожидание загрузки страницы
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'body')))
