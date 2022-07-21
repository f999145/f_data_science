from datetime import datetime

some_date = datetime (2022,8,3)
now_date = datetime.now()
a = some_date - now_date
print (f'{a.days//7} недели и {a.days%7} дня')