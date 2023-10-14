numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
One = numbers[:4]
Two = numbers[5:]
Sum1 = sum(One)
Sum2 = sum(Two)
Girl = len(numbers)
Man = Sum1 + Sum2
Now = Man / Girl
numbers[4] = Now
print("Измененный список:", numbers)
