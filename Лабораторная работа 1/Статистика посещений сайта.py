users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
Had = set(users)
Ynic = len(Had)
Norm = len(users)
dict_users = {"Общее количество": Norm, "Уникальные посещения": Ynic}
print(dict_users)
