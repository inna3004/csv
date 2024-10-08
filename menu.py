from register import get_user_input
from register import logining
from register import read_csv
from register import validate
from register import write_csv


def main() -> None:
    menu = ("\n"
            "    Выберите действие:\n"
            "    1 - Вход\n"
            "    2 - Регистрация\n"
            "    ")
    while True:
        choice = int(input(menu))
        if choice == 1:
            read_csv()
            logining(get_user_input())
        elif choice == 2:
            read_csv()
            try:
                validate(get_user_input())
            except Exception as ex:
                print(ex)
            res = write_csv(get_user_input())
            if res:
                print("пол..")
        else:
            print("Работа с меню завершена")
