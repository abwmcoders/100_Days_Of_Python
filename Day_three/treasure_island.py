print('Welcome to treasure island')

print(''' 
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print('Welcome to treasure island\nYour mission is to find the reasure: ')
cross_road = input('You are at a cross road, where did you want to go, type "right" or "left": ').lower()

if cross_road == 'right':
    print("You fell into a hole, Game over")
elif cross_road == 'left':
    decision = input('You have come to a lake. there is an island at the middle type "wait" to wait for a boat or "swim" to swim across: ').lower()
    if decision == 'swim':
        print('You got attacked by an angry shark, GAME OVER')
    elif decision ==  "wait":
          take_a_door = input('You arrived at the island unarmed. There is a house with three doors "RED, BLUE, YELLOW" which color did you want to open: ').lower()
          if take_a_door == 'blue':
               print("It's a room full of beasts, Game over.")
          elif take_a_door == 'red':
               print("It's a room full of fire, Game over")
          elif take_a_door == 'yellow':
              print("You found the treassure, you win 💫💫💫")
          else:
              print('You lose, GAME OVER')
    else:
        print("Invalid input")
else:
    print("Incalid input")                        
              
