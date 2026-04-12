n = int(input ("Введите длину числа")) #задает длину

user_list = []
i = 0
while i < n:
    string = "Enter element #" + str(i + 1) + ": " #добавляет к числу 1 и добавляет нужное количество
    user_list.append(input(string))
    i += 1

print(user_list)

