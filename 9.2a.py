#!/usr/bin/env python3
"""
Задание 9.2a
Сделать копию скрипта задания 9.2
Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
ключи: имена интерфейсов, вида 'FastEthernet0/1'
значения: список команд, который надо выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_dict.
Ограничение: Все задания надо выполнять используя только пройденные темы.
def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }
"""




def generate_trunk_config(trunk):# создаем функцию


    trunk_template = ['switchport trunk encapsulation dot1q',
              'switchport mode trunk',
              'switchport trunk native vlan 999',
              'switchport trunk allowed vlan'] 
    d_call = {}# создаем словарь
    for inter, vlan in trunk.items():
        d_call[inter] = []# добавляем по ключу пустое значение
        for template in trunk_template:# проходим по списку trunk_template
            if template.endswith('allowed vlan'):# если оканчивается на allowed vlan

                vlan = [str(num) for num in vlan]# меняем циклом тип данных цифры на символы

                vlan = ','.join(vlan)# преобразуем список в строку

                d_call[inter].append(template + ' {}'.format(vlan))# добавляем значение к ключу эл списка trunk_template+ значение со словаря аргумента функции
            else:
                d_call[inter].append(template)# добавляем значение к ключу эл списка trunk_template+
    print(d_call)
    return(d_call)
trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_dict)# вызываем функцию
