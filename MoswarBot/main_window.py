import time
from datetime import datetime

from constants import CONST_LOGIN_INTO_GAME, CONST_PLAY_MOSCOWPOLY, CONST_PLAY_PVP, CONST_DO_TOWER, CONST_DO_ICECREAM, \
    CONST_HOROSCOPE
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QToolBar, QPlainTextEdit, QLineEdit, QPushButton, QComboBox
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import QTimer
import random

LOGIN = 'o.borodin@list.ru'
PASSWORD = '42x5JVH5Sr37ee7'


class MainWindow(QMainWindow):
    def __init__(self, url):
        """
        Initializes the MainWindow class.

        Args:
            url (str): The URL to load in the web view.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Moswar Assistant')
        self.__init_all()
        self.__set_url(url)
        self.toolbar = QToolBar(self)
        self.ui.menuTools.addAction(self.toolbar.toggleViewAction())
        self.view.load(self.url)
        self.__add_text_to_log("Запуск")

    def __init_all(self):
        self.__create_view()
        self.__initialize_execution_button()
        self.__init_log()
        self.__init_open_tasks()
        self.__init_url_line()

    def __initialize_execution_button(self):
        self.ui.button_exec.clicked.connect(self.__on_execution_clicked)

    def __on_execution_clicked(self):
        self.__add_text_to_log("Кнопка нажата")
        self.action = self.ui.code.currentText()
        self.__run()

    def __set_url(self, url):
        self.url = url
        self.url_le.setText(url)

    def __init_open_tasks(self):
        self.ui.code.addItems([CONST_LOGIN_INTO_GAME, CONST_PLAY_MOSCOWPOLY, CONST_PLAY_PVP, CONST_DO_TOWER,
                               CONST_DO_ICECREAM, CONST_HOROSCOPE])

    def __init_log(self):
        self.simple_log = QPlainTextEdit()

    def __init_url_line(self):
        self.url_le = QLineEdit()

    def __create_view(self):
        """
        Creates the web view and sets it as the central widget.
        """
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

    def __run(self):
        """
        Runs the application by loading the web view with the specified URL.
        """
        #self.view.loadFinished.connect(self.__on_load_finished)
        self.__do_task_when_loaded()
        self.__set_url(self.url_le)

    def __on_load_finished(self, ok):
        """
        Callback function for when the web view finishes loading.

        Args:
            ok (bool): Indicates whether the web view loaded successfully or not.
        """
        if ok:
            self.simple_log.appendPlainText("Выполняем задачу: " + self.action)
            self.__wait()
            self.__do_task_when_loaded()
        else:
            print("Error: Failed to load page")

    def __do_task_when_loaded(self):
        self.__wait()
        if self.action == CONST_LOGIN_INTO_GAME:
            self.__fill_login_form()
        elif self.action == CONST_PLAY_MOSCOWPOLY:
            self.__play_moscowpoly()
        elif self.action == CONST_PLAY_PVP:
            pass
        elif self.action == CONST_DO_TOWER:
            pass
        elif self.action == CONST_DO_ICECREAM:
            pass
        elif self.action == CONST_HOROSCOPE:
            pass

    def __play_moscowpoly(self):
        self.__home_click()
        self.__wait()
        # Wait 1 second
        self.__moscowpoly_click()
        for i in range(3):
            self.__add_text_to_log("Попытка " + str(i))
            self.__wait()
            self.__drop_dices()
            self.__wait()
            self.__wait()
            self.__wait()
            self.__activate_dice()
            self.__wait()

    def __drop_dices(self):
        self.__add_text_to_log("Кидаю кубик")
        self.view.page().runJavaScript('document.querySelector(".moscowpoly-drop-dices").click();')
        self.__wait()

    def __activate_dice(self):
        self.__add_text_to_log("Проверяю кнопку активации награды в Москвополии")
        self.view.page().runJavaScript('document.querySelector(".moscowpoly-info-button") !== null;',
                                       self.__activate_dice_exists)
        self.__wait()
        if self.activate_dice_exists:
            self.__add_text_to_log("Кликаю на кнопку активации награды в Москвополии")
            # Выполняем JavaScript для нажатия кнопки
            self.view.page().runJavaScript('document.querySelector(".moscowpoly-info-button").click();')
            self.__wait()
        else:
            print("Button not found on the page")

    def __activate_dice_exists(self, exists):
        if exists:
            self.activate_dice_exists = True
        else:
            self.activate_dice_exists = False

    def __add_text_to_log(self, text):
        """
        Добавляет текст в журнал с указанием текущего времени.
        """
        current_time = datetime.now().strftime("%H:%M:%S")  # Получаем текущее время в формате "ЧЧ:ММ:СС"
        formatted_text = f"[{current_time}] {text}"  # Добавляем текущее время к тексту
        self.ui.simple_log.appendPlainText(formatted_text)

    def __fill_login_form(self):
        """
        Fills the login form with the predefined LOGIN and PASSWORD values.
        """
        try:
            self.__add_text_to_log("Заполняю логин и пароль")
            # Заполняем форму логина
            self.view.page().runJavaScript(f'document.getElementById("login-email").value = "{LOGIN}";')
            self.view.page().runJavaScript(f'document.getElementById("login-password").value = "{PASSWORD}";')
            self.__add_text_to_log("Кликаю на кнопку входа")
            self.view.page().runJavaScript('document.querySelector(\'input[type="submit"]\').click();')
        except Exception as e:
            print("Error:", str(e))

    def __home_click(self):
        self.__add_text_to_log("Кликаю в Хату")
        self.view.page().runJavaScript('document.querySelector("a.home").click();')
        self.__wait()

    def __moscowpoly_click(self):
        self.__add_text_to_log("Кликаю в Москвополию")
        self.view.page().runJavaScript('document.querySelector(".moscowpoly-home__button").click();')
        self.__wait()

    def __on_login_finished(self, success):
        """
        Callback function for when the login process finishes.

        Args:
            success (bool): Indicates whether the login was successful or not.
        """
        if success:
            print("Login successful.")
        else:
            print("Login failed.")

    def __wait(self):
        delay = random.randint(3, 7)  # Генерируем случайное значение времени ожидания от 1 до 5 секунд
        self.__add_text_to_log(f"Жду {delay} секунд")
        time.sleep(delay)
