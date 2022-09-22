print('Welcome to treasure hunt game')

row1 = ['🕸', '🕸', '🕸']
row2 = ['🕸', '🕸', '🕸']
row3 = ['🕸', '🕸', '🕸']

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
place = input('Enter the index to place your treasure: ')
horizontal = int(place[0])
vertical = int(place[1])
map[vertical -1][horizontal -1] = 'X'
print(f"{row1}\n{row2}\n{row3}")