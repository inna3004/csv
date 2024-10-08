import csv
import re


def read_csv():
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        result = list(reader)
        return result


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


def validate_1(user_input: dict):
    pattern = re.compile(r"^\S+@\S+\.\S+$")
    is_valid = pattern.match(user_input["email"])
    if is_valid:
        return True
    if not is_valid:
        raise Exception("Invalid input")
    print(is_valid is not None)

def validate_2(user_input: dict):
    users = read_csv()
    if user_input["login"] in [user["login"] for user in users] and user_input["email"] in [user["email"] for user in users]:
        return True
    else:
        raise Exception("Такой пользователь уже существует.")



def write_csv(user_input: dict):
    new_user = user_input.copy()
    with (open('users.csv', 'a', encoding="utf8", newline='') as csvfile):
        fieldnames = ["login", "password", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_user)
    return True


def logining(user_input: dict):
    keys = user_input.keys()
    if "login" in keys and "password" in keys:
        for user in read_csv():
            if user_input["login"] == user["login"] and user_input['password'] == user["password"]:
                return True
            else:
                return False
