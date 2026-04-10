### if 5 == 5:
###    print("Yes")
###    print("!!!")

user_data = int(input("ВВедите число(цифорки)"))

isHappy = True

#if isHappy == True   одно и то же что и ниже
#    print("Юзверь счастлив")

if isHappy and user_data == 6: #система из 2 условий if первое and добавляет второе#
    print("Юзверь счастлив")
elif user_data == 5:           # elif всегда по середине между if и else
    print("ЧИСЛО всеже 5!")
elif user_data == 7:
    print("ЧИСЛО всеже 7!")
else:
    print("Юзверь несчастен")

##if user_data != 5:
##    print("Мы на месте")
##    if user_data > 6:
##        print("Number is bigger than 5")
