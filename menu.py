from register import read_csv
from register import get_user_input
from register import validate
from register import write_csv
from register import login

menu = '''
Выберите действие:
1 - Регистрация
2 - Вход
'''

while True:
    choice = int(input(menu))
    if choice == 1:
        write_csv()
    elif choice == 2:
        login()
    else:
        print("Работа с меню завершена")
