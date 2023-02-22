'''
BMI = weight / height ** 2
'''
print('Welcome to advanced Bmi calculaotr')

player_height = float(input('Enter your height: '))
player_weight = float(input('Enter your weight: '))

result = round(player_weight / player_height ** 2)
if result < 18.5:
    print('Yello, you are under weight needs vitamin')
elif result < 25:
    print('Yello, you have a normal weight')
elif result < 30:
    print('Yello, you are over weight')    
elif result < 35:
    print('Yello, you are obese')        
else:
    print('Yello, you are clinical obese')  
