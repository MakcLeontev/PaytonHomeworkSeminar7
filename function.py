# Задание в группах: Создать телефонный справочник с возможностью импорта и 
# экспорта данных формате .txt.
def write_in_phonebook(info):
    with open ('Phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
    print('Запись успешно добавлена')

def read_in_phonebook(number):
    with open ('Phonebook.txt', 'r', encoding = 'utf-8') as data:
        x=data.read().split('\n\n\n')
        if number==3:
            for i in range (len(x)):
                print(x[i]) 
                print()
                print()
        else:
            name=input('Введите имя\n')
            inbook=True
            for i in range(len(x)):
                if name in x[i]:
                    print(x[i])
                    inbook=False
            if inbook:
                print('данные отстутствуют')

def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите номер телефона: ')        
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info