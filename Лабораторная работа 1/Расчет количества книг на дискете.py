# TODO Найдите количество книг, которое можно разместить на дискете
A = 25 #Символов в строке
B = 50 #Строк на странице
C = 100 #Число страниц
Mg = 1.44
Bait = (Mg * 1024) * 1024
Z = round(Bait)
Symbol = (B*A)*C # Общее количество символов
V = Symbol * 4
Col = Z // V

print("Количество книг, помещающихся на дискету:", Col)
