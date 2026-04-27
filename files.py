# data = input("Enter a number: ")
# file = open("text.txt", "a")
#
# file.write(data + "\n")
# file.write('Hello!\n')
#
#
# file.close()

file =open("text.txt", "r")
#print(file.read(10))
for line in file: print(line, end="")

file.close()