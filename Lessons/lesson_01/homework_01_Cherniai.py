# task 01 == Виправте синтаксичні помилки
print("Task 1")
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("--------")
print("Task 2")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("--------")
print("Task 3")
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("--------")
print("Task 4")
apples = 2
banana = apples * 4
print(f"Apples - {apples}, bananas - {banana}!")

# task 05 == виправте назви змінних
print("--------")
print("Task 5")
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
print("--------")
print("Task 6")
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f'Perimetery - {perimetery}')


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
print("--------")
print("Task 7")
apples = 4
peers = apples + 5
plums = apples - 2
trees = apples + peers + plums
print(f"Total trees - {trees}")
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

# task 08
print("--------")
print("Task 8")
morning_t = 5
afternoon_t = morning_t - 10
evening_t = afternoon_t + 4
print(f"Evening temperature is ({evening_t})")
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

# task 09
print("--------")
print("Task 9")
total_boys = 24
total_girls = total_boys // 2
today_boys = total_boys - 1
today_girls = total_girls - 2
today_kids = today_boys + today_girls
print(f"{today_kids} kids are present today")
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

# task 10
print("--------")
print("Task 10")
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total_prise = book_1 + book_2 + book_3
print(f"Prise of all three books is {total_prise} UAH")
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
