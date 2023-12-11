import random
from common import *


class Country:
    def __init__(self, name: str, leader: str, population: int):
        self.name = name
        self.leader = leader
        self.attributes = {
            'population': population,
            'happiness': 0,
            'money': 0,
            'food': 0,
            'education': 0,
            'health': 0,
            'culture': 0,
            'society': 0,
            'army': 0,
            'religion': 0,
            'birth_rate': 0,
            'death_rate': 0,
            'immigration_rate': 0,
            'emigration_rate': 0
        }

    def get_name(self):
        return self.name

    def get_leader(self):
        return self.leader

    def get_attribute(self, attribute):
        return self.attributes[attribute]

    def attributes_change(self, current_date):
        [getattr(self, f'_{key}_change')(current_date) for key in self.attributes if hasattr(self, f'_{key}_change')]

    def _population_change(self, current_date):
        """
        Change the population attribute based on the current date.
        """
        # Use a more realistic model for population growth
        population_increase = int(self.attributes[population] * self.attributes[birth_rate]) + int(
            self.attributes[population] * self.attributes[immigration_rate])
        population_decrease = int(self.attributes[population] * self.attributes[death_rate]) + int(
            self.attributes[population] * self.attributes[emigration_rate])
        self.attributes[population] += population_increase - population_decrease

    def _happiness_change(self, current_date):
        """
        Method to calculate the change in happiness based on current date and other attributes of the country.
        """
        # implement logic to change happiness attribute based on current date and other attributes
        happiness_increase = self.attributes[health] + self.attributes[education] + self.attributes[society]
        self.attributes[happiness] += happiness_increase

    def _money_change(self, current_date):
        """
        This method updates the money attribute based on the country's economy, population, and other factors.
        """
        economic_factor = int(self._calculate_economic_factor(self.attributes[money]))
        new_money = self.attributes[money]
        # Calculate the new value based on economic_factor
        new_money *= int(economic_factor)
        # Update the money attribute
        self.attributes[money] = new_money
        # Добавить деньги от налогов в зависимости от количества жителей
        self.attributes[money] += int(self.attributes[population] * 0.53)
        # 0.13 заменить на налоговую ставку
    def _calculate_economic_factor(self, money):
        """
        This method calculates the economic factor based on the country's money and population.
        """
        # TODO: рассмотреть больше факторов, влияющих на приток денег
        if money == 0:
            money += random.randint(1, 3)
        if money == 0 or self.attributes[population] == 0:
            return 0
        return int(money / self.attributes[population])

    def _food_change(self, current_date):
        """
        This method updates the food attribute based on the current date and other attributes of the country.
        """
        # Calculate the change in food attribute based on other attributes
        food_change = self.attributes[population] * self.attributes[education]
        # Update the food attribute
        self.attributes[food] += food_change

    def _education_change(self, current_date):
        """
        This method updates the education attribute based on the current date, population, money, and culture.
        """
        # implement logic to change education attribute based on current date, population, money, culture, etc.
        education_increase = self.attributes[population] * int(self.attributes[money]) * self.attributes[culture]
        self.attributes[education] += education_increase

    def _health_change(self, current_date):
        """
        Method to change the health attribute based on the current date, population, food, and education.
        """
        # implement logic to change health attribute based on current date
        health_increase = 0
        health_increase += int(self.attributes[population] * self.attributes[food] * self.attributes[education])
        self.attributes[health] += health_increase

    def _culture_change(self, current_date):
        """
        This method updates the culture attribute based on the country's education, society, and religion attributes.
        """
        # implement logic to change culture attribute based on current date
        culture_increase = self.attributes[education] + self.attributes[society] + self.attributes[religion]
        self.attributes[culture] += culture_increase

    def _society_change(self, current_date):
        """
        Update the society attribute based on the current date.
        This method implements the logic to change the society attribute of the country based on the current date. It should be called periodically to update the society attribute.
        """
        # implement a more realistic model for society change
        society_change = self.attributes[education] + self.attributes[culture] + self.attributes[health]
        self.attributes[society] += society_change

    def _army_change(self, current_date):
            """
            Calculate the change in army attribute based on current date.
            """
            # implement logic to change army attribute based on current date
            army_change = int(self.attributes[population] * self.attributes[money] * self.attributes[society])
            self.attributes[army] = army_change

    def _religion_change(self, current_date):
        """
        This method updates the religion attribute based on other attributes or factors.
        """
        # Calculate religion_change based on other attributes
        religion_change = self.attributes[education] + self.attributes[society] + self.attributes[culture]
        # Update the religion attribute
        self.attributes[religion] += religion_change

    def _birth_rate_change(self, current_date):
        """
        This method updates the birth rate based on various factors such as health, education, and society attributes of the country.
        """
        # Calculate the factors based on health, education, and society attributes
        health_factor = self.attributes[health] / self.attributes[population]
        education_factor = self.attributes[education] / self.attributes[population]
        society_factor = self.attributes[society] / self.attributes[population]
    
        # Update the birth rate by averaging the factors
        self.attributes[birth_rate] += int((health_factor + education_factor + society_factor) / 3)

    def _death_rate_change(self, current_date):
        health_factor = self.attributes[health] / self.attributes[population]
        food_factor = self.attributes[food] / self.attributes[population]
        education_factor = self.attributes[education] / self.attributes[population]
        # Calculate the death rate based on factors such as health, food, and education
        death_rate = int((health_factor + food_factor + education_factor) / 3)
        self.attributes[death_rate] = death_rate

    def _immigration_rate_change(self, current_date):
        """
        This method updates the immigration rate based on certain factors.
        """
        if self.attributes[food] > 0:
            # Calculate immigration rate based on realistic factors
            if self.attributes[population] != 0:
                economic_factor = self.attributes[money] / self.attributes[population]
                political_factor = self.attributes[society] / self.attributes[population]
                social_factor = self.attributes[culture] / self.attributes[population]
                self.attributes[immigration_rate] += int((economic_factor + political_factor + social_factor) / 3)
        else:
            self.attributes[immigration_rate] = max(0, self.attributes[immigration_rate] - random.uniform(0.01, 1))

    def _emigration_rate_change(self, current_date):
        """
        Update the emigration rate based on realistic factors.
        """
        # TODO: Подумать об отдельном методе для этих факторов и их дальнейшем применении в других методах
        # Calculate emigration rate based on realistic factors
        happiness_factor = self.attributes[happiness] / self.attributes[population]
        money_factor = self.attributes[money] / self.attributes[population]
        food_factor = self.attributes[food] / self.attributes[population]
        education_factor = self.attributes[education] / self.attributes[population]
        health_factor = self.attributes[health] / self.attributes[population]
        culture_factor = self.attributes[culture] / self.attributes[population]
        society_factor = self.attributes[society] / self.attributes[population]
        army_factor = self.attributes[army] / self.attributes[population]
        religion_factor = self.attributes[religion] / self.attributes[population]
        birth_rate_factor = self.attributes[birth_rate] / self.attributes[population]
        death_rate_factor = self.attributes[death_rate] / self.attributes[population]
        immigration_rate_factor = self.attributes[immigration_rate] / self.attributes[population]

        # Update the emigration rate by averaging the factors
        self.attributes[emigration_rate] += int((happiness_factor + money_factor + food_factor + education_factor + health_factor + culture_factor + society_factor + army_factor + religion_factor + birth_rate_factor + death_rate_factor + immigration_rate_factor) / 12)

    def take_money(self):
        # Взять денег взаймы
        self.attributes[money] += 100
    def give_money(self):
        pass