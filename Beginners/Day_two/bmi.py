# this code calculate the bmi of a person
print('Welcome to our bmi calculator')
height = input('Enter your height\n')
weight = input('Enter your weight\n')
result = float(weight) / float(height) ** 2
c = round(result, 2)
print('Your BMI is ' + str(c))