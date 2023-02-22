print('Welcome to leap year generator! ')

'''
    divisible by 4 ---> leap year
    divisible by 100 ---> not leap year
    divisible by 400 ---> leap year

'''
leap_year = int(input('Enter the year: '))
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print(f'year {leap_year} is a leap year')
        else:
            print(f'year {leap_year} is not leap year')
    else:
        print(f'the year {leap_year} is a leap year')    
else:
    print(f'the year {leap_year} is not leap year')                
