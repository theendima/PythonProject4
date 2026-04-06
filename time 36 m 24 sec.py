number = 5 #int целое число integer
digit = 1.5 #float
mem = -1.23456789 #float
bolean = True #bool
bollean = False #bool
word ="Результат:" #string строка с текстом
str_num = "5" #string строка

print(number + int(str_num))
print(word, digit) # word + digit работать не будет так как  данные формата строчки не соединябюбтся с флоатом
print(word + str(mem)) # берет число и преобразует в строку
del number #  удаляет переменную number
number = 7
print("результат :", number)
print(number + int(str_num)) # преобразование  строчки в целое ("5") и сложение
print(word +str(number + int(str_num))) # все в строчночном формате  и переводе скобок в строчный формат после того как флоат передеолается в целое
#int целое число # float дробное #string  строчка текста или цифр #bool - правида лии лож булевая функция