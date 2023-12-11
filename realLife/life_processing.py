import random
from PySide6.QtCore import QDate

from country import Country


class Country_Life():
    def __init__(self, country_name, leader_name):
        self.country = Country(country_name, leader_name, random.randint(10, 100))
        # set random date without time
        self.date = QDate.currentDate()

    def get_country(self):
        return self.country.get_name()

    def get_leader_name(self):
        return self.country.get_leader()

    def get_attribute(self, attribute):
        return self.country.get_attribute(attribute)

    def date_change(self):
        # change the date by 1 day
        self.date = QDate.addDays(self.date, 1)
        # TODO: прогнать остальные события
        self.country.attributes_change(self.date)


    def get_date(self):
        return self.date

    def take_money(self):
        self.country.take_money()

    def get_instance(self):
        return self

    @staticmethod
    def set_instance(self, instance):
        self = instance
