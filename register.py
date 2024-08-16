import csv
import re


def read_csv():
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_user_input():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    email = input("Введите email: ")
    user_input = {
        'login': login,
        'email': email,
        'password': password
    }
    return user_input


def validate(user_input: dict):
    pattern = re.compile(r"^\S+@\S+\.\S+$")
    is_valid = pattern.match(user_input["email"])
    if not is_valid:
        raise Exception("Invalid input")
    print(is_valid is not None)
    if user_input["login"] in [user['login'] for user in read_csv()] or user_input["email"] in [user['email'] for user
                                                                                                in read_csv()]:
        print("Такой пользователь уже существует.")
        return


def write_csv(user_input: dict):
    new_user = user_input.copy()
    with (open('users.csv', 'a', newline='') as file):
        writer = csv.writer(file)
        writer.writerow(new_user)
    print("Пользователь успешно зарегистрирован.")


def login(new_user: dict):
    for user in read_csv():
        if new_user['login'] == user["login"] and new_user['password'] == user["password"]:
            print("Вход выполнен успешно.")
            return
    print("Неверное имя пользователя или пароль.")


def main() -> None:
    menu = ("\n"
            "    Выберите действие:\n"
            "    1 - Регистрация\n"
            "    2 - Вход\n"
            "    ")

    while True:
        choice = int(input(menu))
        if choice == 1:
            read_csv()
            get_user_input()
            validate()
            write_csv((get_user_input())
)
        elif choice == 2:
            login(get_user_input())
        else:
            print("Работа с меню завершена")

if __name__== "__main__":
    main()
