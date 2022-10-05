def daily_skincare_routine():
    print("Welcome to your daily skincare routine!")
    time = (input("Is it morning or evening? Please enter 'morning' or 'evening'. ")).lower()
    if time == 'morning':
        routine = '''1. Cleanse
2. Vitamin C on dry skin
3. Hyaluronic Acid on damp skin
4. Moisturise
5. Sunscreen'''
        print(routine)
        print("Have a great day!")
    else:
        yesterday = (input("What routine did you do yesterday? ")).lower()
        if yesterday == 'exfoliate':
            routine = '''1. Cleanse
2. Retinol - Matrixyl Serum
3. Moisturise'''
        elif yesterday == 'retinol':
            routine = '''1. Cleanse
2. Hyaluronic Acid
3. Moisturise
4. Oil'''
        elif yesterday == 'recovery':
            routine = '''1. Cleanse - Avene
2. Chemical Exfoliate
3. Moisturise'''
        else:
            print("Entry not valid.")
        print(routine)
        print("Good night & sweet dreams!")
        

daily_skincare_routine()
