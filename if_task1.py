age = int(input("Сколько тебе лет? "))

def human_status(input_age):
    if age <= 7:
        return "Ты ходишь в детсад" 
    elif 7 < age <= 16:
        return "Ты школьник"
    elif 16 < age <= 23:
        return "Ты студент"
    else:
        return "Ты работаешь или пенсионер"
print(human_status(age))



    

