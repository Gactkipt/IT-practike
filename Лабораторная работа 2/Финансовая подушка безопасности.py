money_capital= 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital > spend:
    money_capital = money_capital + salary
    if month != 1:
        percent = increase * spend
        spend = spend + percent
    money_capital = money_capital - spend
    month = month + 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
