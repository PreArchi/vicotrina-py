import time

score = 0


def welcome():
    print("Привет! Вы играйте в викторину\n")


# Вопросы
def question(text, answer):
    global score
    print(text)
    if input("Ваш ответ:") == answer:
        print("Верно!")
        score += 1
    else:
        print("Неверно!")


# Сохранение очков
def save_score(score):
    print("Давайте занесём вашу игру в счётчик баллов!")
    player = input("Введите Ваше имя: ")
    record = (player, score)
    print("Подождите...")
    time.sleep(3)
    line = '{0} {1}\n'.format(record[0], record[1])
    with open('scores.txt', 'a') as f:
        print(line, file=f)
        print("Вы были занесены в таблицу!")


# Показывает результаты предыдущих игр.
def show_scores():
    try:
        scores_file = open("scores.txt", "r")
    except IOError:
        print("Файл с таблицей результатов не найден.")
    else:
        print("\nТаблица:")
        for line in scores_file.readlines():
            line = line.strip()
            print(line)


def game():  # Игра викторина
    welcome()
    time.sleep(2)
    f = open("quest.txt")  # открывает файл
    for i in f.readlines():  # Считывает из файла одну строку и возвращает её. (В данном случае, пока строчки не закончатся)

        text, answer = i.strip().split(" ")
        question(text, answer)  # слева текст, справа ответ
    f.close()
    print("Конец викторины! Ваш результат:", score)
    save_score(score)


def main_menu():
    choice = None
    while choice != "0":
        print(
            """
        Игра "Викторина"
        0 - Играть
        1 - Выход
        2 - Результаты прошлых игр

        Автор кода: dankkaaa & vitalkaaa
        """)
        choice = input("Выберите, что вы хотите сделать:")
        # Игра
        if choice == "0":
            game()
        # Выход
        elif choice == "1":
            print("Пока!")
            break
        elif choice == "2":
            print("Подождите...")
            time.sleep(2)
            show_scores()
        # Если
        else:
            print("В меню нет пункта:", choice)


main_menu()
input("\n\nНажмите Enter, чтобы выйти.")  # Выход из программы
