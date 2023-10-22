salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
debt = 0 # долг
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range (1, months + 1):
    if month != 1:
        percent = increase * spend
        spend = spend + percent
    debt = debt + spend
income = month * salary
capital = debt - income
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital,2))
