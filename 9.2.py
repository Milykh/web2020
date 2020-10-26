#!/usr/bin/env python3
"""
Задание 9.2
Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов.

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):

{ 'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17] }
Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
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

    lists = []# создаем пустой список

    #список по условию задачи
    trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan'] 
    for inter, vlan in trunk.items():  # проходим по элементам словаря
        lists.append('interface {}'.format(inter)) #добавляем в конец списка interface+ ключ словаря
        for template in trunk_template:
          if template.endswith('allowed vlan'):# если оканчивается на allowed vlan\
              
              vlan = [str(num) for num in vlan] # меняем циклом тип данных цифры на символы
              
              vlan = ','.join(vlan)# преобразуем список в строку
              
              lists.append(template + ' {}'.format(vlan))# то добавляем в конец списка list  из trunk_template+ строка символов vlan
          else:
              lists.append(template)#то добавляем в конец списка list  из trunk_template
    print(lists)
    return lists
# словарь согласно условию
trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_dict)# вызываем функцию
