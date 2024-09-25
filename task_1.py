# import Queue

# Створити чергу заявок
# queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок


from queue import Queue

queue = Queue()

def generate_request():
    new_request = input("Введіть заявку: ")
    queue.put(new_request)
    print(f"Заявка '{new_request}' додана до черги")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється заявка: {request}")
    else:
        print("Черга пуста")

if __name__ == "__main__":
    while True:
        action = input("Введіть '1' для додавання заявки, '2' для обробки заявки, або 'q' для виходу: ")
        if action == '1':
            generate_request()
        elif action == '2':
            process_request()
        elif action == 'q':
            print("Програма завершена.")
            break
        else:
            print("Невірна команда, спробуйте ще раз.")