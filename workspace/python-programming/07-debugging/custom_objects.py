class User:
    def __init__(self, name, email, country):
        self._name = name
        self._email = email
        self._country = country

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def country(self):
        return self._country

class Employee:
    def __init__(self, name, experience, salary):
        self.__name = name
        self.__experience = experience
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    def get_bonus(self):
        bonus = (self.__salary/self.__experience) * 1000