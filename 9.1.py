#!/usr/bin/env python3
"""
Задание 9.1
Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает, как аргумент, словарь access-портов, вида:

{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17,
 'FastEthernet0/17':150}
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
Проверить работу функции на примере словаря access_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
"""





def generate_access_config(access):# создаем функцию
    lists = []# сщздаем пустой список
    
    # создаем список 
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))# добавляем в список lists ключи  записываем в формате interface FastEthernet...
        for template in access_template:# проходим по списку access_template
            if template.endswith('access vlan'):# если оканчивается на access vlan
                lists.append(template + ' {}'.format(vlan)) # то добавляем в конец списка list  элемент списка access_template + значение со словаря
            else:
                lists.append(template)# иначе добавляем только  элемент списка access_template
    return lists # функция возвращает 

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
lists = generate_access_config(access_dict)# передаем функции словарь 
print(lists)#распечатываем результат работы функции

