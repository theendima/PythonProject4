# # for i in range(1, 10, 3):
# #        print(i)


# coubt = 0
# world = "Hello world"
# for i in world:
#     if i == "H":
#         coubt += 1
# print("Количество", coubt)



# isHasCar = True
#
# while isHasCar:
#     if input("Enter?11111") == "Stop":
#         isHasCar = False




# i = 5
# while i <=15: #  будет выводить цифры до тех пор пока i меньше 15"
#      print(i)
#      i += 2



# for i in range(1, 11):
#     if i >=5: # выводит все до  числа 5
#         break
#
#     if i % 2 == 0: # выводит все что не делится на 2
#             continue
#
#     print(i)


found = None
for i in "Hello":
    if i == "l":
        found = True
        break
else:
    found = False
print(found)