import functions
import sys


def menu():
    print("С помощью цифры выберите команду:\n '1': Найти общих друзей у 2-х случайных человек по ID")
    choice = input()
    if choice == '1' or choice == '"1"':
        functions.get_friendlist()
    elif choice == 'exit':
        sys.exit()
    else:
        print('Error')

while True:
    print("\n")
    menu()
