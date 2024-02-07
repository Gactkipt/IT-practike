# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Motorcycle:
    def init(self, name: str, color: str):
        """название марки"""
        self.name = name
        """цвет Мотоцикл"""
        self.color = color
    def move(self):
        """
 Метод, описывающий движение машины
 >>> Motorcycle = Motorcycle("Мотоцикл", "Черный")
 >>> Motorcycle.move()
        """
        ...

    """Метод, описывающий остановку мотоцикл"""
    def stop(self):
        ...

class Dog:
    def init(self, name: str, age: int, breed: str):
        """имя Собаки """
        self.name = name
        """возраст Собаки"""
        self.age = age
        """порода Собаки"""
        self.breed = breed

    def feed(self, food: str):
        """
 Метод, описывающий кормление собаки
 :param food: еда для кормления
 >>> Dog = Dog("Собака", 2, "Хаски")
 >>> Dog.feed("Мясо")
        """
        ...

    """Метод, описывающий игру с собакой"""
    def play(self, toy: str):
        ...


class Bank_card:
    def init(self, account_number: str, balance: float):
        """номер банковской карты"""
        self.account_number = account_number
        """текущий баланс на карте"""
        self.balance = balance
        """минимальная сумма снятия"""
        self.minsum = 10

    def deposit(self, amount: float):

 """Метод пополнение банковской карты"""
        if amount <= 0:
            raise ValueError("Пополняемая сумма должна быть больше нуля")

    def withdraw(self, amount: float) -> str:
        """Метод, описывающий снятие денег с банковского счета
        :param amount: сумма снятия
        Примеры:
        >>> account = Bank_card("8911523674", 5000.0)
        >>> account.withdraw(100.0)
        "Со счета 8911523674 списано 100.0 руб."
        """
        if amount < self.minsum:
            raise ValueError("Сумма снятия должна быть больше или равна минимальной")
        if self.balance >= amount:
            self.balance -= amount
            return f"Со счета {self.account_number} списано {amount} руб."
        else:
            raise ValueError("Недостаточно средств на счете")
if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
