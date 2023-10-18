# TODO Найдите количество книг, которое можно разместить на дискете
Characters_per_line = 25 #Символов в строке
Lines_per_page = 50 #Строк на странице
Number_of_pages = 100 #Число страниц
Mg = 1.44
Bait = round((Mg * 1024) * 1024)
Symbol = (Lines_per_page * Characters_per_line) * Number_of_pages # Общее количество символов
V = Symbol * 4
Col = Bait // V

print("Количество книг, помещающихся на дискету:", Col)
