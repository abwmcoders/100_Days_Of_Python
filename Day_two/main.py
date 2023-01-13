print("Hello"[3])
print(123_3_566) #automatically ignore the under score for inegers
print('Hello_world')

# Arithmetic operation (PEMDAS)
1 + 1
1 - 1
9 * 2
3 / 4
5 ** 3 # Power or exponential

print(5 // 3)


inputed_number = input('Enter a two digit number: ')

if len(inputed_number) < 2:
    print("Un expected input")

first_num = inputed_number[0]
second_num = inputed_number[1]


result = int(first_num) + int(second_num)
print(result)

