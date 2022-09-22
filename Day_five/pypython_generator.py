import  random
print('Welcome to pypython generator program')

lettters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' 'o',
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
      'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

symbols = ['#', '*', '!', '$', ')', '%', '@', '+', '(', '±', '~']   

hw_letters = int(input('How many letters did you want to have in your password: '))
hw_digits = int(input('How many numbers did you want to have in your password: '))
hw_symbols = int(input('How many symbols did you want to have in your password: '))
random_letters = []
for i in range(1,hw_letters + 1):
    rand_index = random.randrange(len(lettters))
    i = lettters[rand_index]
    random_letters.append(i)
password = ''.join(random_letters)    
print(f'This is letters {password}')    
for i in range(1,hw_digits + 1):
    rand_index = random.randrange(len(numbers))
    i = numbers[rand_index]
    random_letters.append(i)
password = ''.join(random_letters)   
print(f'This is numbers {password}')   
for i in range(1,hw_symbols + 1):
    rand_index = random.randrange(len(symbols))
    i = symbols[rand_index]
    random_letters.append(i)
random.shuffle(random_letters)    
password = ''.join(random_letters)
print(f'Your password is {password}')      

