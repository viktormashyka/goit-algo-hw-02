# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи 
# до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, 
# щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, 
# так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

from collections import deque

d = deque()

def check_palindrome():
    new_string = input("Введіть рядок: ")
    new_string = new_string.lower().replace(" ", "")
    d.append(new_string)
    print(f"Введено рядок: '{new_string}'")
    if new_string == new_string[::-1]:
        print("Рядок є паліндромом")
    else:
        print("Рядок не є паліндромом")

if __name__ == "__main__":
    while True:
        check_palindrome()
        action = input("Введіть 'q' для виходу або будь-яку клавішу для продовження: ")
        if action == 'q':
            print("Програма завершена.")
            break
        else:
            continue