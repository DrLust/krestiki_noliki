from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from common import *


class View(QMainWindow):
    def __init__(self, country):
        super().__init__()
        self._set_country(country)
        self.labels = []
        # Создание окна
        self.setWindowTitle("Игра - Симулятор страны")
        # set background picture
        background_image = QLabel(self)
        pixmap = QPixmap("background.jpg")
        background_image.setPixmap(pixmap)
        background_image.resize(window_width, window_height)
        self.resize(window_width, window_height)
        # Создание вертикального layout
        self.layout = QVBoxLayout()
        # Наполняем экран
        self.layout.addWidget(QLabel(f'Название: {self.country.get_country()} '))
        self.layout.addWidget(QLabel(f'Президент: {self.country.get_leader_name()} '))
        self.layout.addWidget(QLabel(f'Население: {self.country.get_attribute(population)} человек '))
        self.layout.addWidget(QPushButton(f'Взять взаймы', clicked=self.country.take_money))
        self.layout.addWidget(QLabel(f'Деньги: {self.country.get_attribute(money)} рублей '))
        self.layout.addWidget(QLabel(f'Текущая дата: {self.country.get_date().toString("dd.MM.yyyy")}  '))
        self.layout.addWidget(QLabel(f'Количество еды: {self.country.get_attribute(food)} картошки '))
        self.layout.addWidget(QLabel(f'Уровень счастья: {self.country.get_attribute(happiness)} улыбок '))
        self.layout.addWidget(QLabel(f'Уровень здоровья: {self.country.get_attribute(health)} белоснежных зубов '))
        self.layout.addWidget(QLabel(f'Уровень образования: {self.country.get_attribute(education)} биномов Ньютона '))
        self.layout.addWidget(QLabel(f'Уровень культуры: {self.country.get_attribute(culture)} балетов '))
        self.layout.addWidget(
            QLabel(f'Уровень религиозности общества: {self.country.get_attribute(religion)} молитв в день '))
        self.layout.addWidget(QLabel(f'Уровень общества: {self.country.get_attribute(society)} взаимопомощи '))
        self.layout.addWidget(QLabel(f'Уровень армии: {self.country.get_attribute(army)} грозных штыков '))
        self.layout.addWidget(QLabel(f'Уровень рождаемости: {self.country.get_attribute(birth_rate)} детей в день '))
        self.layout.addWidget(QLabel(f'Уровень смертности: {self.country.get_attribute(death_rate)} смертей в день '))
        self.layout.addWidget(
            QLabel(f'Уровень миграции: {self.country.get_attribute(immigration_rate)} мигрантов в день '))
        self.layout.addWidget(
            QLabel(f'Уровень эмиграции: {self.country.get_attribute(emigration_rate)} эмигрантов в день '))
        self._create_timer()
        # Установка layout в окне
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def _create_timer(self):
        # set timer for date changing
        self.timer = QTimer()
        self.timer.timeout.connect(self._event_processing)
        self.timer.start(TIMER_INTERVAL)

    def _set_country(self, country):
        self.country = country.get_instance()

    def _event_processing(self):
        try:
            self.country.date_change()
        except Exception as e:
            print(f"An error occurred while processing the event: {e}")

        # Get label with date from self.layout
        label = self.layout.itemAt(DATE_LABEL_INDEX).widget()
        if label:
            label.setText(f'Текущая дата: {self.country.get_date().toString("dd.MM.yyyy")}  ')
        else:
            print("Отсутствует виджет для отображения даты")

        population_label = self.layout.itemAt(POPULATION_LABEL_INDEX).widget()
        if population_label:
            population_label.setText(f'Население: {self.country.get_attribute(population)} человек ')
        else:
            print("Отсутствует виджет для отображения населения")

        money_label = self.layout.itemAt(MONEY_LABEL_INDEX).widget()
        if money_label:
            money_label.setText(f'Деньги: {self.country.get_attribute(money)} рублей ')
        else:
            print("Отсутствует виджет для отображения денег")

        immigration_label = self.layout.itemAt(IMMIGRATION_RATE_LABEL_INDEX).widget()
        if immigration_label:
            immigration_label.setText(
                f'Уровень миграции: {self.country.get_attribute(immigration_rate)} мигрантов в день ')
        else:
            print("Отсутствует виджет для отображения уровня миграции")