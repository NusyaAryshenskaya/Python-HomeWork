def show_phonebook():
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for i in data:
        print(i)
    file.close()


def create_contact():
    file = open('phonebook.txt', 'a', encoding='UTF-8')
    data = input('Введите данные ФИО, телефон, комментарий (через ;): ')
    file.write('\n' + data)
    file.close()
    print("Контакт добавлен")


def find_contact():
    find_data = input("Введите данные для поиска контакта: ")
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_data in item:
            print(item)
    file.close()


def change_contact():
    show_phonebook()
    change_data = input("Введите данные для редактирования контакта: ")
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for i in range(len(data)):
        if change_data in data[i]:
            print(f"{data[i]} \n Этот контакт редактируем? Если правильно, то введите 'да' иначе любое слово")
            temp = input()
            if temp == 'да':
                list1 = data[i].split(';')
                j = int(input("Введите '1', если хотите отредактировать ФИО,'2' если контакт или '3' если комментарий: "))
                list1[j - 1] = input('Введите новые данные: ')
                data[i] = ";".join(list1)
                if j == 3:
                    data[i] += "\n"
                print("Данные изменены")
    file.close()

    file = open('phonebook.txt', 'w', encoding='UTF-8')
    for item in data:
        file.write(item)
    file.close()


def del_contact():
    del_data = input("Введите данные: ")
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if del_data in item:
            data.remove(item)
            print(f"Контакт {item[0]} удален")
    file.close()

    file = open('phonebook.txt', 'w', encoding='UTF-8')
    for item in data:
        file.write(item)
    file.close()


print(
    'Главное меню\n''1. Просмотреть контакты\n''2. Создать контакт\n''3. Найти контакт\n''4. Изменить контакт\n''5. Удалить контакт\n''6. Выход\n')

flag = True

while flag:

    choose = int(input("Выберите пункт: "))

    if choose == 1:
        show_phonebook()

    if choose == 2:
        print("Создание контакта")
        create_contact()

    if choose == 3:
        print("Поиск контакта")
        find_contact()

    if choose == 4:
        print("Редактирование контакта")
        change_contact()

    if choose == 5:
        print("Удаление контакта")
        del_contact()

    if choose == 6:
        print("Выход")
        flag = False