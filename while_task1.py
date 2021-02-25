while True:
    try: 
        hello_user = input('Как дела? ')
        if hello_user == 'Хорошо':
            print ('Это я и хотел узнать. До свидания!')
            break 
    except KeyboardInterrupt: 
        print("Пока")
        break

    
