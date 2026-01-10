print(f"Enter your symbols: ")
text = input()
symbols_count = len(set(text))

if symbols_count <= 10:
    print(symbols_count, False)
else:
    print(symbols_count, True)

# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
