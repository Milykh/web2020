#!/usr/bin/env python3
"""
Задание 9.1a
Сделать копию скрипта задания 9.1.

Дополнить скрипт:

ввести дополнительный параметр, который контролирует будет ли настроен port-security
имя параметра 'psecurity'
по умолчанию значение False
Проверить работу функции на примере словаря access_dict, с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
"""





def generate_access_config(access, psecurity=False):# создаем функцию

    lists = []# сщздаем пустой список

# создаем список 
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']


    port_security = ['switchport port-security maximum 2',
                 'switchport port-security violation restrict',
                 'switchport port-security']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))# добавляем в список lists ключи  записываем в формате interface FastEthernet...
        for template in access_template:# проходим по списку access_template
            if template.endswith('access vlan'):# если оканчивается на access vlan
                lists.append(template + ' {}'.format(vlan))# то добавляем в конец списка list  элемент списка access_template + значение со словаря
            else:
                lists.append(template)# иначе добавляем только  элемент списка access_template
        for sec_1 in port_security:
            if psecurity: #проверяем дополнительный параметр
                lists.append(sec_1)# добавляем в конец списка
    return lists

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
lists = generate_access_config(access_dict)
print(lists)# вывод по умолчанию


lists = generate_access_config(access_dict,True)
print(lists)# вывод если psecurity=True
