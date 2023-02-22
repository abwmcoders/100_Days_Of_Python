# this code calculate tip
print('Welcome to our tip calculator app')
bill = input('How much bill are you in $ ')
tip_given = input('how many tip did you want to give: 10%, 20%, 30%, 40%...')
total_to_pay = input('how many people are sharing the bill: ')
calc = float(bill) * float(tip_given) / 100
print(calc)
total = (calc + float(bill)) / int(total_to_pay)
estimate = round(total, 2)
print (f'each person is to pay the sum ${estimate}')
