"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():

    now = datetime.now()    
    yesterday = now - timedelta(days=1)
    print(yesterday)
    print(now)
    month_ago = now-timedelta(days=30)
    print(month_ago)


    


def str_2_datetime(date_string):
    
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
