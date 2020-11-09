import datetime

year, month, day = input().split(' ')
days = int(input())
d = datetime.date(int(year), int(month), int(day))
delta = datetime.timedelta(days=days) # дельта в 2 дня
c = d + delta
print(c.year, c.month, c.day) # Узнаем какое число будет через 2 дня