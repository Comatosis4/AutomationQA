def sum_numbers(string):
    try:
        numbers = string.split(",")
        n = 0
        for num in numbers:
            n += int(num)
        return n
    except ValueError:
        return 'Не числове значення'

list1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for i in list1:
    print(sum_numbers(i))