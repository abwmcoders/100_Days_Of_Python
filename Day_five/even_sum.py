print('Welcome to the even numbers addition between 1 to 100')
# number divisible by 2 without a remainder ==> even number
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum)

# another way
add = 0
for i in range(0, 101, 2):
    add += i
print(add)