#!/usr/bin/env python3
"""
Задание 9.4
Создать функцию, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!', а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Ограничение: Все задания надо выполнять используя только пройденные темы.
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)
"""





ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
   
    return any(word in command for word in ignore)#Возвращает True, если в команде содержится слово из списка ignore, False - если нет



def get_config(config):
    config_dict = {}# создаем пустой словать
    with open(config, 'r') as file:#открываем файл на чтение
        for line in file:
            if ignore_command(line, ignore) or line.find('!') != -1:# проверяем на содержание слов из списка и !
                continue
            else:
                if line.startswith(' '):#начинается ли строка с указанного префикса' '
                    slave = line.strip()#возвращаем копию строки
                    config_dict[main].append(slave)# Добавляем значение по ключу
                else:
                    main = line.strip()#возвращаем копию строки
                    config_dict[main] = []# по ключу записываем пустое значение
    return config_dict
all_1 = get_config('D:/P_Y_T_H_O_N_WEB/z9/config_sw1.txt')#


print(all_1)