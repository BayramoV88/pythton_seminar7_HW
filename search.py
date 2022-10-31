from all_contacts import all_contacts

def search(pb):
    print('Критерии поиска: \n1. фамилия\n2. номер телефона \n')
    choice = int(input('Введите желаемый критерий поиска: '))
    temp = []
    check = -1
    if choice == 1:
        sel = str(input('Введите фамилию контакта: '))
        for i in range(len(pb)): 
            if sel in pb[0]:
                check = i
                temp.append(pb[i])
        print(temp)
    elif choice == 2:
        sel = str(input('Введите номер телефона: '))
        for i in range(len(pb)):
            if sel in pb[2]:
                check = i
                temp.append(pb[i])
        print(temp)
    else:
        all_contacts(temp)
        return check