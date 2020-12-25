def input_str():
    return str(input())


def var_check(counter_i, counter_j, text_for_person, var, opt):
    if var in {1, 13, 14, 15, 16, 18}:
        return counting_numbers(counter_i, text_for_person, var - 1, opt)
    elif var in {2, 3, 5, 6}:
        return text(counter_i, text_for_person, var - 1, opt)
    elif var in {4, 8, 12}:
        return bool_check(counter_i, text_for_person, var - 1, opt)
    elif var in {7, 9, 10, 11}:
        return tags(counter_i, text_for_person, var - 1, opt)
    elif var in {17}:
        return range_of_numbers(counter_i, counter_j, text_for_person, var - 1, opt)


def counting_numbers(counter_i, text_for_person, var, opt):
    opt.extend(text_for_person)
    print('Выберете тип выполнения: [1]:Одиночный / [2]:Диапазон ')
    var_temporary = input_str()
    if var_temporary == '1':
        print('Введите данные: ')
        person_choice = input('')
        for _ in opt:
            if opt[counter_i][var] != person_choice:
                text_for_person.remove(opt[counter_i])
            counter_i += 1
    elif var_temporary == '2':
        print('Введите данные: ')
        print('Минимальное значение: ')
        min = int(input())
        print('Максимальное значение: ')
        max = int(input())
        for _ in opt:
            if float(opt[counter_i][var]) < min or float(opt[counter_i][var]) > max:
                text_for_person.remove(opt[counter_i])
            counter_i += 1
    return text_for_person


def text(counter_i, text_for_person, var, opt):
    opt.extend(text_for_person)
    print('Введите данные: ')
    person_choice = input_str()
    for _ in opt:
        if opt[counter_i][var] != person_choice:
            text_for_person.remove(opt[counter_i])
        counter_i += 1
    return text_for_person


def tags(counter_i, text_for_person, var, opt):
    opt.extend(text_for_person)
    print('Введите данные: ')
    person_choice = input_str()
    for _ in opt:
        if person_choice not in opt[counter_i][var]:
            text_for_person.remove(opt[counter_i])
        counter_i += 1
    return text_for_person


def range_of_numbers(counter_i, counter_j, text_for_person, var, opt):
    opt.extend(text_for_person)
    print('Введите данные: ')
    print('Минимальное значение: ')
    min = int(input())
    print('Максимальное значение: ')
    max = int(input())
    text_min = ''
    text_max = ''
    check = True
    for i in opt:
        for j in i:
            if counter_j == var:
                for z in j:
                    if z == '-':
                        check = not check
                    elif check == 1:
                        text_min += z
                    else:
                        text_max += z
                check = not check
            counter_j += 1
        if not (int(text_min) >= min and int(text_max) <= max):
            text_for_person.remove(opt[counter_i])
        text_min = ''
        text_max = ''
        counter_j = 0
        counter_i += 1
    return text_for_person


def bool_check(counter_i, text_for_person, var, opt):
    opt.extend(text_for_person)
    yes = 'да'
    no = 'нет'
    print('Да/Нет: ')
    person_choice = input_str()
    if person_choice.lower() == yes:
        for _ in opt:
            if opt[counter_i][var] != '1':
                text_for_person.remove(opt[counter_i])
            counter_i += 1
    elif person_choice.lower() == no:
        for _ in opt:
            if opt[counter_i][var] != '0':
                text_for_person.remove(opt[counter_i])
            counter_i += 1
    return text_for_person


def dialogue_table(text_for_person):
    counter_i = 0
    counter_j = 0
    result = open('result.txt', 'tw', encoding='utf-8')
    while True:
        print('[1]appid         \t[2]name         \t[3]release_date     \t[4]english          \t[5]developer\n')
        print('[6]publisher     \t[7]platforms    \t[8]required_age     \t[9]categories       \t[10]genres\n')
        print('[11]steamspy_tags\t[12]achievements\t[13]positive_ratings\t[14]negative_ratings\t[15]average_playtime\n')
        print('[16]median_playtime\t[17]owners      \t[18]price\n')
        print('                                                         \t\t[19]CONFIRM         \t[20]CANCEL\n')
        print("Выберете вариант: ")
        var = int(input())
        opt = []
        if 1 <= var <= 18:
            text_for_person = var_check(counter_i, counter_j, text_for_person, var, opt)
        elif var == 19:
            for i in text_for_person:
                result.write(' '.join(i))
                result.write('\n')
            break
        elif var == 20:
            break
    result.close()
