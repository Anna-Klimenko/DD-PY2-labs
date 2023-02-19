class Serial:
    """Базовый класс - сериал"""
    def __init__(self, name: str, episodes_number: int, rating: float):
        """
        Создание и подготовка к работе базового класса "Сериал"
        :param name: Название сериала
        :param episodes_number: Количество серий
        :param rating: Оценка зрителей
        """
        self._name = name  # Название сериала изменить нельзя

        if not isinstance(episodes_number, (int)):
            raise TypeError("Количество серий должно быть типа int")
        if episodes_number <= 0:
            raise ValueError("Количество серий должно быть положительным числом")
        self._episodes_number = episodes_number  # Количество серий изменить нельзя

        if not isinstance(rating, (float)):
            raise TypeError("Оценка зрителей должна быть типа float")
        if rating <= 0:
            raise ValueError("Оценка зрителей должна быть положительным числом")
        self.rating = rating

    def __str__(self) -> str:
        """
        Магический метод __str__
        :return: Возвращает название сериала, количество серий и оценку зрителей
        """
        return f"Сериал {self.name}. Количество серий {self.episodes_number}. Оценка зрителей {self.rating}."

    def __repr__(self) -> str:
        """
        Магический метод __repr__
        :return: Возвращает название сериала, количество серий и оценку зрителей
        """
        return f"{self.__class__.__name__}(name={self._name!r}, episodes_number={self._episodes_number!r}, rating={self.rating!r})"

    def episodes_number_left(self, episodes_number: int, viewed_episodes_number: int) -> int:
        """
        Метод определяет сколько серий осталось просмотреть
        :param episodes_number: Количество серий сериала всего
        :param viewed_episodes_number: Число просмотренных серий
        :return: Число оставшихся серий
        """
        if not isinstance(viewed_episodes_number, (int)):
            raise TypeError("Число просмотренный серий должно быть типа int")
        if viewed_episodes_number <= 0:
            raise ValueError("Число просмотренный серий должно быть положительным числом")
        return episodes_number - viewed_episodes_number

    @property
    def name(self) -> str:
        """
        Свойство делает атрибут только для чтения. Причина инкапсуляции - нельзя менять название сериала
        :return: Название сериала
        """
        return self._name

    @property
    def episodes_number(self) -> int:
        """
        Свойство делает атрибут только для чтения. Причина инкапсуляции - нельзя менять количество серий
        :return: Количество серий сериала
        """
        return self._episodes_number


class Sitcom(Serial):
    """Дочерний класс сериала - ситком
    Магические методы __str__ и __repr__ перегружены, т.к. добавляется новый атрибут theme
    Метод episodes_number_left наследуется
    """
    def __init__(self, name: str, episodes_number: int, rating: float, theme: str):
        """
        Создание и подготовка к работе дочернего класса "Ситком"
        :param name: Название сериала
        :param episodes_number: Количество серий сериала
        :param rating: Оценка зрителей
        :param theme: Тематика ситкома
        """
        super().__init__(name, episodes_number, rating)
        self._theme = theme  # Тематику ситкома изменять нельзя

    def is_about_vampires(self, theme) -> bool:
        """
        Метод определяет являются ли тематикой ситкома вампиры
        :param theme: Тематика ситкома
        :return:  Являются ли тематикой ситкома вампиры
        """
        if theme == "Vampires":
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Магический метод __str__
        :return: Возвращает название сериала, количество серий, оценку зрителей и тематику ситкома
        """
        return f"Сериал {self.name}. Количество серий {self.episodes_number}. Оценка зрителей {self.rating}. Тематика {self.theme}."

    def __repr__(self) -> str:
        """
        Магический метод __repr__
        :return: Возвращает название сериала, количество серий, оценку зрителей и тематику ситкома
        """
        return f"{self.__class__.__name__}(name={self._name!r}, episodes_number={self._episodes_number!r}, rating={self.rating!r}, theme={self._theme!r})"

    @property
    def theme(self) -> str:
        """
        Свойство делает атрибут только для чтения. Причина инкапсуляции - нельзя менять тематику ситкома
        :return: Тематика ситкома
        """
        return self._theme


if __name__ == "__main__":
    serial = Serial("Friends", 236, 9.2)
    print(serial)
    print(serial.episodes_number_left(236, 100))
    print(serial.__repr__())

    sitcom = Sitcom("What we do in the shadows", 40, 8.1, "Vampires")
    print(sitcom)
    print(sitcom.is_about_vampires("Vampires"))
    print(sitcom.episodes_number_left(40, 15))
    print(sitcom.__repr__())
    pass
