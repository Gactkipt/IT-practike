# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, share = ','):
    unity = set(first.split(share))&set(second.split(share))
    return sorted(list(unity))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group,participants_second_group,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
