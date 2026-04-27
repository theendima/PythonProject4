# import time # встроенный модуль
#
# time.sleep(5) # вызываем модул ьс джоп ко нмадной + указывааем задуржку сколько бюудет ждать (5секунд)
# print("спим 5 сек")
# import datetime as dt # вызвали модуль дата тайм и переименовали его в dt
#
# day = dt.datetime.today().time()  #вызвал переменную и запросил  сегодня/ сейчас уточнил что нужно  время
# print(day)

# import datetime as d, sys, os, platform, random
# print(sys.path)
# print(os.name)
# print(platform.system())
# print(random())

# from math import sqrt as dd, ceil # из модуля импортируем  часть функций используем фром и что импортируем
# print(dd(100))

# import mymodule as my
# print(my.name)
# my.hello()

from mymodule import add_three_numbers as add

print(add(5,6,1))

import cowsay as c
c.cow("Hello")

