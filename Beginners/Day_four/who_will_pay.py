import random
print('Welcome to who will pay program')
names = input('Enter the names of your gang separated with comma(,)and space: ')
li = names.split(', ')
name_lenght = len(li)
payer = random.randint(0, name_lenght - 1)
final = li[payer - 1]
print(f"{final} is going to pay the bill")
