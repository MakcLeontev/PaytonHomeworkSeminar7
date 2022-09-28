from function import get_info, write_in_phonebook, read_in_phonebook


def start():
    choise=int(input('Здравствуйте, что вы хотите сделать?\n1.Записать в телефонную книгу\n2.Найти контакт\n3.Посмотреть всю книгу\n'))
    if choise==1:
        n=get_info()
        write_in_phonebook(n)
    elif choise==2:
        read_in_phonebook(2)
    else:
        read_in_phonebook(3)
  