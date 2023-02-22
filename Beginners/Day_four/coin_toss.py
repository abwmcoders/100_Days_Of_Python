import random
from main import random_alg


print('Welcome to our coin toss program')
print(random_alg)

side = random.randint(0,1)
if side == 1:
    print('Heads')
else:
    print('Tails')    