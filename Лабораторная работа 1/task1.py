import doctest

class ChristmasLights:
    def __init__(self, bulbs_number: int, brightness_level: int, color: str):
        """
        Создание и подготовка к работе объекта "Новогодняя гирлянда"
        :param bulbs_number: Количество светящихся лампочек
        :param brightness_level: Максимальный уровень яркости гирлянды
        :param color: Цвет гирлянды

        Примеры:
        >>> christmas_lights = ChristmasLights(50, 10, 'white')
        """
        if not isinstance(bulbs_number, int):
            raise TypeError("Количество светящихся лампочек должно быть типа int")
        if bulbs_number < 0:
            raise ValueError("Количество светящихся лампочек не может быть отрицательным числом")
        self.bulbs_number = bulbs_number

        if not isinstance(brightness_level, int):
            raise TypeError("Уровень яркости должен быть int")
        if brightness_level <= 0:
            raise ValueError("Уровень яркости должен быть положительным числом")
        self.brightness_level = brightness_level

        if not isinstance(color, str):
            raise TypeError("Цвет гирлянды должен быть типа str")

    def are_lights_on(self) -> bool:
        """
        Функция проверяет включена ли гирлянда
        :return: Включена ли гирлянда
        Примеры:
        >>> christmas_lights = ChristmasLights(50, 10, 'white')
        >>> christmas_lights.are_lights_on()
        """
        ...

    def add_brightness(self, added_brightness: int) -> None:
        """
        Увеличить уровень яркости гирлянды
        :param added_brightness: Выбранный уровень яркости
        :raise ValueError: Если выбранный уровень яркости превышает максимальный, то вызываем ошибку
        :return:
        Примеры:
        >>> christmas_lights = ChristmasLights(50, 10, 'white')
        >>> christmas_lights.add_brightness(5)
        """
        if not isinstance(added_brightness, int):
            raise TypeError("Выбранный уровень яркости должен быть int")
        if added_brightness < 0:
            raise ValueError("Уровень яркости не может быть отрицательным числом")
        ...

class Wireless_Headphones:
    def __init__(self, charge_percentage: int, battery_time: int):
        """
        Создание и подготовка к работе объекта "Беспроводные наушники"
        :param charge_percentage: Процент заряда
        :param battery_time: Время работы батареи в часах

        Примеры:
        >>> wireless_headphones = Wireless_Headphones(90, 5)
        """
        if not isinstance(charge_percentage, int):
            raise TypeError("Процент заряда должен быть типа int")
        if charge_percentage < 0:
            raise ValueError("Процент заряда не может быть отрицательным числом")
        if charge_percentage > 100:
            raise ValueError("Процент заряда не может быть больше 100")
        self.charge_percentage = charge_percentage

        if not isinstance(battery_time, (int, float)):
            raise TypeError("Время работы батареи должно быть типа int или float")
        if battery_time < 0:
            raise ValueError("Время работы батареи не может быть отрицательным числом")
        self.battery_time = battery_time

    def charge_headphones(self, percents) -> None:
        """
        Зарядить наушники на определенное число процентов
        :param percents: Число процентов заряда
        :raise ValueError: Если число процентов, на которое зарядились наушники, превышает 100, то вызываем ошибку
        :return: Число процентов, на которое зарядились наушники
        Примеры:
        >>> wireless_headphones = Wireless_Headphones(90, 5)
        >>> wireless_headphones.charge_headphones(10)
        """
        if not isinstance(percents, int):
            raise TypeError("Число процентов заряда должно быть типа int")
        if percents < 0:
            raise ValueError("Число процентов заряда не может быть отрицательным числом")
        ...

    def use_headphones(self, usage_hours) -> None:
        """
        Воспользоваться наушниками для прослушивания музыки
        :param usage_hours: Количество часов использования наушников
        :raise: Если количество часов использования наушников превышает время работы батареи, то вызываем ошибку
        :return: Количество часов использования наушников
        Примеры:
        >>> wireless_headphones = Wireless_Headphones(90, 5)
        >>> wireless_headphones.use_headphones(2.5)
        """
        if not isinstance(usage_hours, (int, float)):
            raise TypeError("Количество часов использования наушников должно быть типа int или float")
        if usage_hours < 0:
            raise ValueError("Количество часов использования наушников не может быть отрицательным числом")
        ...

class CoursePaper:
    def __init__(self, number_of_pages: int, topic: str):
        """
        Создание и подготовка к работе объекта "Курсовая работа"
        :param number_of_pages: Требуемое количество страниц
        :param topic: Тема курсовой работы
        Примеры:
        >>> course_paper = CoursePaper(40, 'Экономика')
        """
        if not isinstance(number_of_pages, int):
            raise TypeError("Требуемое количество страниц должно быть типа int")
        if number_of_pages <= 0:
            raise ValueError("Требуемое количество страниц должно быть положительным числом")

        if not isinstance(topic, str):
            raise TypeError("Тема курсовой работы должна быть типа str")

    def write_course_paper(self, written_pages: int) -> None:
        """
        Писать курсовую работу
        :param written_pages: Количество написанных страниц
        :return: Количество написанных страниц
        Примеры:
        >>> course_paper = CoursePaper(40, 'Экономика')
        >>> course_paper.write_course_paper(15)
        """
        if not isinstance(written_pages, int):
            raise TypeError("Количество написанных страниц должно быть типа int")
        if written_pages < 0:
            raise ValueError("Количество написанных страниц не может быть отрицательным числом")
        ...

    def is_course_paper_written(self) -> bool:
        """
        Функция проверяет написана ли курсовая работа
        :return: Написана ли курсовая работа
        Примеры:
        >>> course_paper = CoursePaper(40, 'Экономика')
        >>> course_paper.is_course_paper_written()
        """
        ...

if __name__ == "__main__":
    doctest.testmod() 
    pass
