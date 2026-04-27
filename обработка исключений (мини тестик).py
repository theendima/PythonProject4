# try:
#     x = int(input("Введи число: "))
#     x += 7
#     print(x)
# except ValueError:
#     print("Введи ЦИФРУ!!!!")


# x = 0
# while x == 0:
#     try:
#         x = int(input("Введи число: "))
#         x += 7
#         print(x)
#     except ValueError:
#         print("Введи ЦИФРУ!!!!")
try:
    y = int(input("ВВеди цифорку"))
    x =  5 / y

except ZeroDivisionError:
    print("Деление на 0")

except ValueError:
    print("Введи цифорку:" )
else:
    print("Результат =", x)
finally:
    print("Ну вот и все Ребята")