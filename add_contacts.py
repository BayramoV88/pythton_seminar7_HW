def add_contact(pb):
    info = []
    for i in range(len(pb[0])):
        if i == 0:
            info.append(input('Введите фамилию: '))
        if i == 1:
            info.append(input('Введите имя: '))
        if i == 2:
            info.append(input('Введите номер телефона: '))
        if i == 3:
            info.append(input('Введите описание: '))
    pb.append(info)
    
    with open('Guide.csv', 'a', encoding='utf-8') as file:
        file.write(f"\nфамилия: {info[0]}\nимя: {info[1]}\nномер телефона: {info[2]}\nописание: {info[3]}\\n")
    return pb