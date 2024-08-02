import csv
from getpass import getpass
import re

def read_csv():
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

    def register():
        login = input("Введите логин: ")
        pattern = re.compile(r"^\S+@\S+\.\S+$")
        email = input("Введите email: ")
        is_valid = pattern.match(email)
        print(is_valid is not None)
        password = getpass("Введите пароль: ")


        if login in [user['login'] for user in read_csv()] or email in [user['email'] for user in read_csv()]:
            print("Такой пользователь уже существует.")
            return

        new_user = {
            'login': login,
            'email': email,
            'password': password
        }
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_user)
        print("Пользователь успешно зарегистрирован.")

    def login():
        login = input("Введите логин: ")
        password = getpass("Введите пароль: ")

        for user in read_csv():
            if user['login'] == login and user['password'] == password:
                print("Вход выполнен успешно.")
                return
        print("Неверное имя пользователя или пароль.")


    menu = '''
    Выберите действие:
    1 - Регистрация
    2 - Вход
    '''

    while True:
        choice = int(input(menu))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        else:
            print("Работа с меню завершена")



