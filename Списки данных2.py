
numbers = [1, 5, 7]
numbers.append(100) #добавление в список 100
numbers.insert(1, True) #заменить позицию на true
b= [10, 20, 30, 40] #добавление
numbers.extend(b)
numbers.sort()

numbers.pop(2)
numbers.remove(100)

#print(numbers.count(10)) # выводит сколько раз у нас "10" в листе
print(len(numbers))  #выводит количество  переменных в листах
print(numbers)