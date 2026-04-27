try:
    with open("file.txt","r",encoding="utf-8") as file: # менеджер with as открываеи и сам закрывает файл
        print(file.read())

except FileNotFoundError:
    print("файл не найден")
