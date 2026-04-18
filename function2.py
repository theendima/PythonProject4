def min1(l):
    min_el = l[0]
    for el in l:
        if el < min_el:
            min_el = el

    return min_el




num1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
min12 = min1(num1)

num2 = [1,3,4.56,5,6,7,8,9,10,11,12,13,2]
min23 = min1(num2)

if min12 < min23:
    print(min12)
else:
    print(min23)




# num2 = [1.0,2.1,3,4.56,5,6,7,8,9,10,11,12,13,2,1,]
# min_el = num2[0]
# max_el = num2[0]
# for el in num2:
#     if el < min_el:
#         min_el = el
#     if el > max_el:
#         max_el = el
# print(min_el)
# print(max_el)