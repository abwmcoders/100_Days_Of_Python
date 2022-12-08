from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_continue = True

while is_continue:
    direction = input("type 'encrypt' to encode, type 'decrypt' to decode a message: \n").lower()

    text = input("Enter your message: ").lower()
    shift = int(input('Enter the number of shift: '))

    def caeser(plain_text, shift_amount, cypher_direction):
        cyphar_text = ''
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                if cypher_direction == 'encrypt':
                    new_position = position + shift_amount
                else:
                    new_position = position - shift_amount   
                new_letter = alphabet[new_position]
                cyphar_text += new_letter   
            else:
                cyphar_text += char      
        print(f'The {cypher_direction} text is "{cyphar_text}"') 

    caeser(plain_text= text, shift_amount= shift, cypher_direction= direction)    

    continue_caeser = input("type 'yes' to continue and 'no' to quit: ").lower() 

    if continue_caeser == 'no':
        is_continue = False
        print("Good bye 🤙")


    #caeser(plain_text= text, shift_amount= shift, cypher_direction= direction)         