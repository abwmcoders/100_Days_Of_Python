print('Welcome to fizzbuzz game')

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz ' + str(number))
    elif number % 3 == 0:
        print('Fizz ' + str(number))
    elif number % 5 == 0:  
        print('Buzz ' + str(number))
    else:
        print(number)          