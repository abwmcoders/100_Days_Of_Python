print('Welcome to pizza ordering app')

size_scale = input('What type of pizza did you want? ("L" for large, "M" for medium, and "S" for small: )').upper()
add_peperoni = input('Did you want peperoni? ("y" / "n")').upper()
add_extra_cheese = input('Did you want extra cheese? ("y" / "n")').upper()

bill = 0
if size_scale == 'L':
    bill += 25
    if add_peperoni == 'Y':
        bill += 3
elif size_scale == 'M':
    bill += 20
    if add_peperoni == 'Y':
        bill += 3
elif size_scale == 'S':
    bill += 15    
    if add_peperoni == 'Y':
        bill += 2
if add_extra_cheese == 'Y':
            bill += 1        
print(f'Your bill is ${bill}')