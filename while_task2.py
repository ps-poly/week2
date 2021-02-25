conversation = {"Привет":"Здарова, отец",
    "Как дела?": "Хорошо",
    "Что делаешь?": "Программирую на Python"}

while True:
    ask_user = input("Введи вопрос: ")
    if ask_user == "Пока":
        print("До свидания!")
        break
    else:
        print(conversation[ask_user])


