
import os
import time

# Цвета для консоли
КРАСНЫЙ = "\033[41m  \033[0m"
БЕЛЫЙ = "\033[47m  \033[0m"
СБРОС = "\033[0m"


# ЗАДАНИЕ 1: Флаг Швейцарии
def flag():
    print("\nЗАДАНИЕ 1: ФЛАГ ШВЕЙЦАРИИ\n")

    for row in range(1, 6):
        for col in range(1, 6):
            if (row, col) in [(2, 3), (3, 2), (3, 3), (3, 4), (4, 3)]:
                print("\033[47m  \033[0m", end="")
            else:
                print("\033[41m  \033[0m", end="")
        print()


# ЗАДАНИЕ 2: Повторяющийся узор
def pattern():
    print("\nЗАДАНИЕ 2: УЗОР\n")

    for i in range(8):
        if i % 2 == 0:
            print("* + * + * + * +")
        else:
            print("+ * + * + * + *")


# ЗАДАНИЕ 3: Анимация из трёх кадров
def animation():
    print("\nЗАДАНИЕ 3: АНИМАЦИЯ\n")

    frames = [
        "   *\n  ***\n *****",
        "  ***\n *****\n*******",
        " *****\n  ***\n   *"
    ]

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print("ЗАДАНИЕ 3: АНИМАЦИЯ\n")
        print(frame)
        time.sleep(1)

    print("Анимация завершена!")
    time.sleep(1)


# ЗАДАНИЕ 4: Диаграмма процентного соотношения чисел
def percentages():
    print("\nЗАДАНИЕ 4: ПРОЦЕНТНАЯ ДИАГРАММА\n")

    with open("sequence.txt", "r", encoding="utf-8") as file:
        numbers = [float(line) for line in file if line.strip()]

    # Первая группа: числа от -3 до 3 включительно
    inside = sum(1 for n in numbers if -3 <= n <= 3)

    # Вторая группа: все остальные числа
    outside = len(numbers) - inside

    total = len(numbers)

    if total == 0:
        print("В файле нет чисел.")
        return

    p1 = inside / total * 100
    p2 = outside / total * 100

    print("Числа от -3 до 3:", inside)
    print("Остальные числа:", outside)
    print(f"Числа от -3 до 3: {p1:.2f}%")
    print(f"Остальные числа: {p2:.2f}%")

    print("\nПроцентная диаграмма:")
    print("От -3 до 3: ", "#" * round(p1 / 2), f"{p1:.2f}%")
    print("Остальные:  ", "#" * round(p2 / 2), f"{p2:.2f}%")


# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: График функции y = x / 3
def graph():
    print("\nДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: ГРАФИК y = x / 3\n")

    height = 9
    width = 27

    for y in range(height, -1, -1):
        line = ""

        for x in range(width + 1):
            if x == 0 and y == 0:
                line += "+"
            elif x == 0:
                line += "|"
            elif y == 0:
                line += "-"
            elif abs(y - x / 3) < 0.01:
                line += "*"
            else:
                line += " "

        print(line)

    print("График функции y = x / 3")


# Запуск всех заданий
animation()
flag()
pattern()
percentages()
graph()
