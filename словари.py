a = {"code": "RUS","name": 'Russia', "region": 'USSR'} # 1 вариант создания словаря
#a = dict (code="RUS", name="Russia", region="Russia") #  2вариант создания словаря
#print(a["code"])
#for key,value in a.items(): print(key, " - ", value) #  пример для перебора словаря
#print(a['code']) # метод вывода по  определенному ключу
#print(a.get("code"))# метод вывода по  определенному ключу
#a.clear() # очистка от всех аргументов
#a.pop("name") # удаление по элементу ключа
#a.popitem() # удаление последнего элемента
# print(a.keys()) # вывод  списка только ключей
# print(a.values()) # вывод  списка только значений
# print(a.items()) # вывод списка кортежем ключ + значение
# a['code'] = "LOL" # переустановка ключа
# print(a.items())

person = { # создал эелемент персона с элементом юзверь
    'user1': {
        '1name': 'John',
        '2name': '1337',
        'age': 75,
        'gender': 'male',
        'adress': ("г. Кишинев", "ул. WHere is?", "228"),
        "grade": {"math":5,"YPK":4, "MVP": 999},
    },

 "user2": {

    }
}
print(person['user1']['adress'][1]) # вывод и адресация точеченого элемента в кортеже
print(person['user1']['adress']) # вывод  и адресация вывода полного картежа



