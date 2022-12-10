import doctest
from typing import Union

class Glass:    # TODO Написать 3 класса с документацией и аннотацией типов
    def __init__(self, capacity_volume: float, occupied_volume: float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку
        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.
        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.
        :return: Объем реально извлеченной жидкости
        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        ...

class Window:
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        """Создание и подготовка к работе объекта класса Window
        :param height: высота Window
        :param width: ширина Window
        Примеры:
        >>> window = Window(200, 60) # инициализация объекта
        """
        if height < 0:
            raise ValueError("Высота Window должна быть положительным числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота Window должна быть int или float")
        self.height = height

        if width < 0:
            raise ValueError("Ширина Window должна быть положительным числом")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина Window должна быть int или float")
        self.width = width

    def open_Window(self) -> bool:
        """Метод, который проверяет открыта ли дверь
        :return является ли дверь открытой
        Примеры:
        >>> window = Window(200,60)
        >>> window.open_Window()
        """
        ...

    def the_presence_of_a_door_handle(self) -> bool:
        """Метод, который проверяет есть ли у двери ручка
        :return есть ли ручка у Window
        Примеры:
        >>> window = Window(200,60)
        >>> window.the_presence_of_a_door_handle()
        """
        ...

class TV:

    def __init__(self, diagonal: Union[int, float], mark: str, volume: int):
        """
        Создание и подготовка к работе объекта класса TV - телевизор
        :param diagonal: диагональ экрана телевизора;
        :param mark: бренд телевизора;
        :param volume: громкость телевизора;
        Примеры:
        >>> television = TV(40,"Phillips",12) # инициализация объекта
        """
        if diagonal < 0:
            raise ValueError("Диагональ экрана телевизора должна быть положительным числом")
        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ экрана телевизора должна быть int или float")
        self.diagonal = diagonal

        if not isinstance(mark, str):
            raise TypeError("Бренд телевизора должен быть типа str")
        self.mark = mark

        if volume < 0:
            raise ValueError("Громкость телевизора должна быть положительным числом")
        if not isinstance(volume, int):
            raise TypeError("Громкость телевизора должен быть типа int")
        self.volume = volume

    def increase_the_volume(self, volume: int) -> None:
        """Метод, который увеличивает громкость телевизора
        :raise ValueError: Если значение громкости больше возможного для данного телевизора, то вызовем ошибку
        Примеры:
         >>> television = TV(40,"Philips",12)
         >>> television.increase_the_volume(18)
         """
        if volume < 0:
            raise ValueError("Громкость телевизора должна быть положительным числом")
        if not isinstance(volume, int):
            raise TypeError("Новое значение громкости телевизора должно быть типа int")
        self.volume = volume

    def turn_on_the_TV(self) -> None:
        """Метод, который включает телевизор
        Примеры:
        >>> television = TV(40,"Philips",15)
        >>> television.turn_on_the_TV()
        """
        ...





if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
