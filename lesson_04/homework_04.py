adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 1")
print(adwentures_of_tom_sawer.replace("\n", " "))

# task 02 ==
""" Замініть .... на пробіл
"""
print("--------")
print("Task 2")
#print(adwentures_of_tom_sawer.replace("\n", " ").replace(" .... ", " "))
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ").replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("--------")
print("Task 3")
adwentures = " ".join(adwentures_of_tom_sawer.split())
print(adwentures)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("--------")
print("Task 4")
number = adwentures.count("h")
print(f"Кількість літер \"h\" в тексті: {number}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("--------")
print("Task 5")
string = adwentures.split()
num = 0
for word in string:
    if word.lstrip().istitle():
        num += 1
print(f'Кількість слів в тексті, що починаються з великої літери - {num}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("--------")
print("Task 6")
index = adwentures.find("Tom", adwentures.find('Tom') + 1)
print(f'Слово \"Tom\" зустрічається вдруге на позиції №: {index}')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("--------")
print("Task 7")
adwentures_of_tom_sawer_sentences = adwentures.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("--------")
print("Task 8")
print('Четверте речення з текста в нижньому регістрі:')
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("--------")
print("Task 9")
# n = 0
for i, sentence in enumerate(adwentures_of_tom_sawer_sentences, start=1):
    if sentence.startswith("By the time"):
        print(f'Речення {i} починається з фрази \"By the time\"')
        # n = 1
    else:
        print(f'Речення {i} не починається з фрази \"By the time\"')
# if  n != 1:
#     print(f'Жодне з речень не починається з фрази \"By the time\"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("--------")
print("Task 10")
adwentures_of_tom_sawer_last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(adwentures_of_tom_sawer_last_sentence)
print(f'Кількість слів в останньому реченні: {len(adwentures_of_tom_sawer_last_sentence.split())}')