numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
left_ = numbers[:4]
right = numbers[5:]
Sum_left = sum(left_)
Sum_right = sum(right)
long = len(numbers)
Summa = Sum_left + Sum_right
Now = Summa / long
numbers[4] = Now
print("Измененный список:", numbers)
