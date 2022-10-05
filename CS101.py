print("Welcome to the skin care routine program!")
day = (input("What day is it today? ")).lower()
#print(day)
def daily_routine(day):
    if day == 'monday' or day == 'wednesday' or day == 'friday':
        return '''Exfoliate
Moisturize'''
    elif day == 'tuesday' or day == 'thursday':
        return '''Exfoliate
Moisturize
Eye Drops'''
    elif day == 'satuday' or day == 'sunday':
        return '''Eat Pizza
Watch Movies
Sleep whenever'''
    else:
        return "Not a valid day. Try again."
print(daily_routine(day))