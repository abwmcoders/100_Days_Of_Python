from art import logo

print(logo)

def calc(num1, num2, input_sign):
    if input_sign == '*':
        return num1 * num2
    elif input_sign == '/':    
        return num1 / num2
    elif input_sign == '-':
        return num1 - num2
    elif input_sign == '+':
        return num1 + num2
    else:
        print('Invalid sign')  


first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
sign = input('enter "*" for multiplication, \n"+" for addition, \n"-" for subtraction and \n"/" for division\n')          


result = calc(num1= first_num, num2= second_num, input_sign= sign)

print(f'{first_num} {sign} {second_num} = {result}')