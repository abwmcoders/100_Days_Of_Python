# this code calculate the remaining life you have left from ur current age

print('Welcome to life in weeks')
age = input('whats your current age\n')
left = 90 - int(age)
life_in_weeks = left * 52
life_in_months = left * 12
life_in_days = left * 365 

print(f'Hey pals, you have {life_in_days} days, {life_in_weeks} weeks and {life_in_months} months left. ')