# Making a Caeser Cipher Encoder and Decoder
# Importing art from art.py 
from art import logo

# Printing the art
print(logo)

# Alphabet list
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# Function for both encoding and decoding
def caeser(original_text, shift_amount, encode_or_decode):
    cipher_text = ""

    # For decoding sepcifically
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Main logic of Caeser Cipher
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter

    # Displaying the ciphered text
    print(f"Here is the {encode_or_decode}d message: {cipher_text}")

# To make the code menu driven and to restart without executing the .py file again
script_complete = False
while not script_complete:

    # Inputs taken by user
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Calling the caeser function
    caeser(text, shift, direction)

    # Here to exit the code we need to type n but for it to continue we can type y or other character or even just press enter again without typing anything the Capital "Y" signifies its the default input
    complete = input("Do you want to restart the program?(Y/n)").lower()

    # To exit the loop if we typed n in the restart line
    if complete == "n":
        script_complete = True
        print("Goodbye")
