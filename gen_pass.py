# coding: utf-8

import random
import zipfile
import shutil

# Распаковка файла (необязательно делать с помощью Python)
task_file = zipfile.ZipFile('task_file.txt.zip') # открываем архив
task_file.extractall() # извлекаем из него все в текущую папку
task_file.close # закрываем архив

# Создание функции для генерации email адресов
def email_gen(list_of_names):  # генерация email принимает список имен list_of_names
    emails = [] # Создаем пкустой список с email
    for i in list_of_names: # для каждого иммени из листка имен
        letter = 1 # при наличии в имени одинаковых букв у объектов (Ивн Ильдар) мы добавляем еще одну букву в e.mail
        if i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io') # берем emails и добавляем в конец имя
        print(emails) # смотрю на результаты
    return emails
email_gen([['ivan', 'makarov'], ['ildar', 'makarov'], ['sahsa','ivanov']])

# Создание функции для генерации паролей
def pass_gen(A):  # генерация пароля
    digits = '1234567890'
    leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leters_2 = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    password = ''
    var = [digits, leters, leters_2, symbols] # переменная содержащая в себе все значения из переменных выше
    password += random.choice(digits)
    password += random.choice(leters)
    password += random.choice(leters_2)
    password += random.choice(symbols)
    while len(password) < A: # до тех пор пока длинна пароля не будет = А
        password += random.choice(var[random.randint(0,3)]) # добавляем к пустой строке по 1 символу из var
    return password
pass_gen(12) # генерация пароля из 12 символов
# Открываем файл и достаем оттуда текст.
# Создаем из строк текста список.
# Далее список нужно очистить.
# И создаем email адреса.
with open('C:/Users/User2/PycharmProjects/exam/task_file.txt', 'r') as f:
    l = f.readline() # читаем файл в переменную l
    print(l)
#     stop_words = ['NaN', 'NO_NAME', 'None'] # список сло от которых необходимо почистить список
    names = []
    other = []
    error = []
    for line in f: # для переменной line в считываемом файле
        s = line.split(', ') # переменной s присваем значения из line уже разделенные запятой
#         print(s)
        s_clean = [x.replace(' ', '') for x in s]  # тут проводим замену пробела на ничего в переменной s значение котрой присваиваем ипеременной s_clean
#         print(s_clean)
        if s_clean[1] != '' and s_clean[2] != '' and s_clean[1].istitle() == True: # далее идет условие, если 1й индекс s_clean не равна ничему 2й тоже и 3й начинается с заглавной буквы
            if len(s_clean[3]) == 7 and s_clean[3].isdigit() == True: # также тут указывается что значения индексов объектов должны = 7 и цифрам
                names.append([s_clean[1], s_clean[2]]) # добавляем все в списки тогда
                other.append([s_clean[1], s_clean[2], s_clean[3], s_clean[4]])
            else:
                names.append([s_clean[1], s_clean[2]])
                other.append([s_clean[1], s_clean[2], 'not_valid_phone_number', s_clean[4]])
        else:
            error.append(s_clean)
emails = email_gen(names)
print(error)

# Записываем информацию в новом файле с ответом
list_l = l.split(',') # далее полученные значения выщеприведенной переменной l разделяется хяпятой и присваиваются пременной list_l
print(list_l)
list_l.insert(1, ' PASSWORD') # в list_l вставляем "столбец",  PASSWORD, по сути он идет не как столбец, а добавление значения в строку к имеющимся данным
print(list_l)
with open ('C:/Users/User2/PycharmProjects/exam/answer_file.txt', 'w') as f: # открываем файл с результатми
    new_l = ', '.join(list_l) # преобразуй нам список в строку
    f.write(new_l) # и запиши его в переменную f
    for i in range(len(names)): # Далее мы создаем цикл и определяем длинну списка
        f.write(emails[i] + ', ' + pass_gen(10) + ', ' + other[i][0] + ', ' + other[i][1] + ', ' + other[i][2] + ', ' + other[i][3]) # после чего записываем данные ранее заполненные в переменные

# Записываем ошибки в отдельный файл
with open ('error_file.txt', 'w') as f:
    for i in error:
        f.write(', '.join(i))

# Проверка результата

# Архивируем папку с ответами (там должен быть файл с кодом, txt файл с ответом и docx файл с отчетом) - Необязательно
shutil.make_archive('C:/Users/User2/PycharmProjects/exam/answer/diplom', 'zip')
