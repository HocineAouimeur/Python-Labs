
import os
import time
from pathlib import Path


# ЗАДАНИЕ 1: Флаг Франции
def flag():
    print("\nЗАДАНИЕ 1: ФЛАГ ФРАНЦИИ\n")

    blue = "\033[44m  \033[0m"
    white = "\033[47m  \033[0m"
    red = "\033[41m  \033[0m"

    for row in range(5):
        print(blue * 5 + white * 5 + red * 5)



# ЗАДАНИЕ 2: Повторяющийся узор A
def pattern():
    print("\nЗАДАНИЕ 2: УЗОР A\n")

    for row in range(3):
        for col in range(3):
            if (row, col) in [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]:
                print("██", end="")
            else:
                print("  ", end="")
        print()


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
        print(frame)
        time.sleep(1)

    print("Анимация завершена!")
    time.sleep(2)


# ЗАДАНИЕ 4: Процентная диаграмма
def percentages():
    print("\nЗАДАНИЕ 4: ПРОЦЕНТНАЯ ДИАГРАММА\n")

    file_path = Path(__file__).parent / "sequence.txt"
    print(file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        numbers = [float(line) for line in file if line.strip()]

    # Первая группа: числа меньше нуля
    negative = sum(1 for n in numbers if n < 0)

    # Вторая группа: числа больше нуля
    positive = sum(1 for n in numbers if n > 0)

    # Нулевые числа не входят ни в одну группу
    total = negative + positive

    if total == 0:
        print("Нет чисел меньше или больше нуля.")
        return

    p1 = negative / total * 100
    p2 = positive / total * 100

    print(f"Числа меньше 0: {negative} ({p1:.2f}%)")
    print(f"Числа больше 0: {positive} ({p2:.2f}%)")

    print("\nПроцентная диаграмма:")
    print("Меньше 0:  ", "#" * round(p1 / 2), f"{p1:.2f}%")
    print("Больше 0:  ", "#" * round(p2 / 2), f"{p2:.2f}%")


# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: График y = x^2
def graph():
    print("\nДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: ГРАФИК y = x^2\n")

    height = 9
    width = 9

    for y in range(height, -1, -1):
        line = ""

        for x in range(width + 1):
            if x == 0 and y == 0:
                line += "+"
            elif x == 0:
                line += "|"
            elif y == 0:
                line += "-"
            elif round(x * x / 9) == y:
                line += "*"
            else:
                line += " "

        print(line)

    print("График функции y = x^2")

    
animation()

# ЗАПУСК ВСЕХ ЗАДАНИЙ
flag()
time.sleep(2)

pattern()
time.sleep(2)


percentages()
time.sleep(2)

graph()
