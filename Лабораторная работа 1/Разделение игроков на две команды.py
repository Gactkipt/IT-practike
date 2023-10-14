list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
Ser = len(list_players) // 2
One = list_players[:Ser]
Two = list_players[Ser:]
print(One)
print(Two)
