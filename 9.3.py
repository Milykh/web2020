#!/usr/bin/env python3
"""Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:
словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
 {'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17]}
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



def get_int_vlan_map(config):# создаем функцию
    with open(config, 'r') as file:# открываем файл на чтение
            access_config = {}#создаем пустые словари
            trunk_config = {}
            for line in file:# проходим файл
                if line.find('FastEthernet') != -1:# если строка найдена( возвращает -1 если не найдена)
                    interface = line.split()[-1]# сохраняем последний элемент списка
                elif line.find('access vlan') != -1:#если строка найдена( возвращает -1 если не найдена)
                    access_vlan = line.split()[-1]# сохраняем последний элемент списка
                    access_config[interface] = access_vlan# в словарь записывает ключ и значение
                elif line.find('trunk allowed vlan') != -1:#если строка найдена( возвращает -1 если не найдена)
                    trunk_vlan = line.split()[-1]# сохраняем последний элемент списка
                    trunk_config[interface] = trunk_vlan# в словарь записывает ключ и значение
                else:
                    pass
            print('access interfaces: \n', access_config)
            print('trunk interfaces: \n', trunk_config)
    return access_config, trunk_config
get_int_vlan_map('D:/P_Y_T_H_O_N_WEB/z9/config_sw1.txt')# вызываем функцию с аргументом имени файла
