
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
