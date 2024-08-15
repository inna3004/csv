from register import write_csv
from register import login



def main()-> None:
    menu = ("\n"
            "    Выберите действие:\n"
            "    1 - Регистрация\n"
            "    2 - Вход\n"
            "    ")

    while True:
        choice = int(input(menu))
        if choice == 1:
            write_csv()
        elif choice == 2:
            login()
        else:
            print("Работа с меню завершена")
