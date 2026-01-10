list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []
for i in list1:
    if type(i) == str:
        list2.append(i)
print(f'Ліст із виділеними стрінговими значеннями: {list2}')