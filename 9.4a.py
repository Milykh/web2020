#!/usr/bin/env python3
"""
Задание 9.4a
Задача такая же, как и задании 9.4. Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл. В нём есть разделы с большей вложенностью, например, разделы:

interface Ethernet0/3.100

router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности. При этом, не привязываясь к конкретным разделам. Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:

то команды верхнего уровня будут ключами словаря,

а команды подуровней - списками

Если уровня вложенности три:

самый вложенный уровень должен быть списком,

а остальные - словарями.

На примере interface Ethernet0/3.100

{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}
Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
​
def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
​
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
​
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
​
    '''
    return any(word in command for word in ignore)
"""





ignore = ['duplex', 'alias', 'Current configuration']
def check_ignore(command, ignore):
    
    return any(word in command for word in ignore)#Возвращает True, если в команде содержится слово из списка ignore, False - если нет




def get_config(config): 
    config_dict = {}# создаем словарь
    lvl_dict = {}#создаем словарь
    lvl1_list = []# создаем список
    fel = None# ставим флаг
    with open(config, 'r') as file: # открываем файл на чтение
        for line in file: 
            value = [] #сщздаем список
            if check_ignore(line, ignore) or line.find('!') != -1: # проверяем на отсутствие слов ignore и !
                continue 
            else: 
                if line[0] == ' ' and line[1] != ' ':#проверяем условия
                    lvl1 = line.strip()#сохраняем строку
                    lvl1_list.append(lvl1)#добавляем в список
                    config_dict[main].append(lvl1)#добавляем в словарь
                elif line[0] == ' ' and line[1] == ' ':#проверяем условия
                    lvl2 = line.strip()#сохраняем строку
                    if fel == None:#проверяем флаг
                        for i in lvl1_list:#
                            lvl_dict[i] = []#создаем ключи словаря
                        config_dict[main] = lvl_dict#добавляем в список
                    config_dict[main][lvl1].append(lvl2)#добавляем в словарь
                    fel = 'blackhall' #меняем флаг
                else: 
                    main = line.strip() #сохраняем строку
                    config_dict[main] = value#добавляем в словарь
                    fel = None# меняем флаг
                    lvl1_list = []# обнуляем список
                    lvl_dict = {}#обнуляем словарь
    return config_dict 
 
all_1 = get_config('D:/P_Y_T_H_O_N_WEB/z9/config_r1.txt')
print(all_1)
