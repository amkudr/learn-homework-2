"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv



def main():
    job = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    {'name': 'Аркадий', 'age': 30, 'job': 'Romantic'}
    ]

    with open('export.csv', 'w', encoding='1251', newline="") as f:        
        fields = ['name', 'age', 'job']             
        writer = csv.DictWriter(f, fields, delimiter=";")        
        writer.writeheader()
        writer.writerows(job)          



if __name__ == "__main__":
    main()
