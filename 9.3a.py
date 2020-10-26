#!/usr/bin/env python3
"""
Задание 9.3a
Сделать копию скрипта задания 9.3.
Дополнить скрипт:
добавить поддержку конфигурации, когда настройка access-порта выглядит так:
interface FastEthernet0/20
  switchport mode access
  duplex auto
То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/20':1 }
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""




def get_int_vlan_map(config):# создаем функцию
    access_config = {}#создаем пустые словари
    trunk_config = {}#создаем пустые словари
    with open(config, 'r') as file:# открываем файл на чтение
        for line in file:# проходим файл
            if line.find('FastEthernet') != -1:# если строка найдена( возвращает -1 если не найдена)
                interface = line.split()[-1]# сохраняем последний элемент списка
                line = file.readline()# читаем строку
                if line.find('mode access') != -1:# если строка найдена( возвращает -1 если не найдена)
                    line = file.readline()# читаем строку
                    access_vlan = line.split()[-1]# сохраняем последний элемент списка
                    if access_vlan.isdigit():# смотрим есть ли в строке цифры
                        access_config[interface] = access_vlan# в словарь записывает ключ и значение
                    else:
                        access_config[interface] = '1'# в словарь записывает ключ и значение '1'
                elif line.find('encapsulation dot1q') != -1:# если строка найдена( возвращает -1 если не найдена)
                    line = file.readline()# читаем строку
                    trunk_vlan = line.split()[-1]# сохраняем последний элемент списка
                    
                    trunk_config[interface] = trunk_vlan# в словарь записывает ключ и значение
        print('access interfaces: \n', access_config)
        print('trunk interfaces: \n', trunk_config)
        return access_config, trunk_config
get_int_vlan_map('D:/P_Y_T_H_O_N_WEB/z9/config_sw2.txt')

