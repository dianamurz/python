n = int(input("Введите число этажей у пирамиды: "))

for i in range(1, n + 1):
    # Пробелы
    for j in range(n - i):
        print(" ", end="")

    # Звёздочки
    for k in range(2 * i - 1):
        print("*", end="")

    print()
