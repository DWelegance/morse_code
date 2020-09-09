import pyperclip

#dictionary with the 26 characters and '/' for spaces
alphabet = {' ': '/','a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-',
            'l': '.-..', 'm': '--', 'n': '-.', 'o':'---', 'p': '.--.', 'q':'--.-',
            'r':'.-.', 's': '...', 't': '-', 'u': '..-', 'v':'...-', 'w':'.--',
            'x':'-..-', 'y':'-.--', 'z':'--..'}
def english_to_morse():
    #creates our lists we use
    decode_list = []
    coded_list = []
    print('Also copies your morse code to clipboard!\n')
    user_input = input("Enter your message to be transfered to morse code!\n")
    #takes every letter in user_input, lowercases it and adds to our decode_list
    for letter in user_input:
        decode_list.append(letter.lower())
    #checks the decode_list to see if any are in the alphabet dictionary
    #if they are it adds the morse_code associated with letter and puts it into our coded list
    for letter in decode_list:
        if letter in alphabet:
            coded_list.append(alphabet[letter])
    #turns our coded_list into a string, prints it, and copys it into clipboard
    #also adds spaces between the morse characters
    string_list = ' '.join(coded_list)
    print(string_list)
    pyperclip.copy(string_list)

def morse_to_english():
    #makes our lists we need and our character counter variable
    #which we use to determine when the user input ends
    morse_code = []
    character_list = []
    translated_list = []
    character_counter = 0
    user_input = input('Enter your morse code to be translated to english!\n')
    #loops through every character in the input while incrementing the char counter
    for character in user_input:
        character_list.append(character)
        character_counter = character_counter + 1
        #breaks when it finds a space and adds it to the morse_code list as a string
        #while removing the space from the string
        if character == ' ':
            morse_string = ''.join(character_list[:-1])
            morse_code.append(morse_string)
            morse_string = []
            character_list = []
        #determines when it has reached the end of the string and adds the final character
        elif character_counter == len(user_input):
            morse_string = ''.join(character_list)
            morse_code.append(morse_string)
    #loops through the morse_code list checking if the values are in our dictionary
    #if they are it adds the key associated with the value and stores it in the translated_list
    for character in morse_code:
        if character in alphabet.values():
            for letter, morse_letter in alphabet.items():
                if character == morse_letter:
                    translated_list.append(letter)
    #turns our list into a string and prints it! all done
    translated_message = ''.join(translated_list)
    print(translated_message)
#sets up our "UI" giving user options on what they would like to do
def user_choice():
    print("This program uses International Morse code and uses '/' to denote spaces")
    print('[1] English to Morse code\n[2] Morse to English\n[3] Exit')
    user_choice = input("Enter the number for what you would like to do\n")
    if user_choice == '1':
        english_to_morse()
    if user_choice == '2':
        morse_to_english()
    if user_choice == '3':
        return 'quit'

#our main loop breaks when the user presses 3 on the UI menu
while True:
    if user_choice() == 'quit':
        print('Goodbye')
        break
