class Tree:
    """
 Класс описывает дерево.
            """
    def __init__(self, age:int, height:int):
        self.age = age
        self.height = height
        """ Объявление экземпляра класса.
 :param age: возраст (сколько лет дереву)
 :param height: высота (какого размера дерево в метрах)
                """

    def __str__(self):
        return f"Tree Age: {self.age}, Tree height: {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.age!r}, {self.height!r})"

    def cut_the_top(self, x:int)-> int:
        """
                 Метод от дерева отрезается кусок дерева длинной "х"
                 :param x: сколько нужно отрезать сверху
                 Пример:
                 >>> tree1 = tree(15, 2)
                 >>> tree1.cut_the_top(0,5)
                 """
        self.height -= x
        return self.height

    def defence(self)-> str:
        """
                 Метод выдает строчку, о способах защищать дерево от вредителей
                        """
        return f"нанести белую краску"


class FruitTree(Tree):
    """
               Класс описывает плодовое дерево.
               """
    def __int__(self, age:int, height:int, fruit:str):
        """ Объявление экземпляра класса.
                        :param age: возраст (годы)
                        :param height: высота (метры)
                        :param fruit: тип плодов
                        """

        super().__init__(age, height)
        self.fruit = fruit

    def __str__(self):
        return f"Tree Age: {self.age}, Tree height: {self.height}, Fruit{self.fruit}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.age!r}, {self.height!r}, {self.fruit!r})"

    def defence(self) -> str:
        """
             Метод выдает строчку, о способах защищать дерево от вредителей
             Данный метод переопределен,т.к. исходный метод не полностью удовлетворяет дочернему классу
                                """
        return f"Необходимо: " \
               f"1) Белить ствол;" \
               f"2) Закрывать низ ствола, от зайцев;" \
               f"3) Закрывать плоды от птиц, с помощью сетки"

if __name__ == "__main__":
    # Write your solution here
    pass