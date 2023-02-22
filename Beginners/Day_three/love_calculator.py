print('Welcome to love calculator')

your_name = input('Whats your name').lower()
partner_name = input('Whats your partner name').lower()

combined_string = your_name + partner_name

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

true = t+r+u+e
love = l+o+v+e

final = str(true) + str(love)
n = int(final)
if n < 10 or n > 90:
    print(f'your love score is {final}, you go together like coke and mentos!.')
elif n == 40 and n <= 50:
    print(f'Your love score is {final}, you are alright together...')   
else:
    print(f'Your love score is {final}')     
