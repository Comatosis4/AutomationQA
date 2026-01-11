list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list1:
    if i % 2 == 0:
        sum += i
print(f'Сума парних значень в лісті = {sum}')