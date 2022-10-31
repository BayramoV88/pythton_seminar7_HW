def init_pb():
    temp = []
    pb = []
    rows = 1
    cols = 5
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                temp.append(str(input('Введите фамилию: ')))
                if temp[j] == '' or temp[j] == ' ':
                    with open('Guide.csv', 'w') as file:
                        file.write(f'фамилия: {temp.append}')
            if j == 1:
                temp.append(str(input('Введите имя: '))) 
                if temp[j] == '' or temp[j] == ' ': 
                    with open('Guide.csv', 'w') as file:
                        file.write(f'имя: {temp.append}')
            if j == 2:
                temp.append(str(input('Введите номер телефона: ')))
            if j == 3:
                temp.append(str(input('Введите описание: ')))
    pb.append(temp)
    print(pb)
    with open('Guide.csv', 'a', encoding='utf-8') as file:
        file.write(f'\nфамилия: {temp[0]}, имя: {temp[1]}, номер телефона: {temp[2]}, описание: {temp[3]}\n')
    return pb