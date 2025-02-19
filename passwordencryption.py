from html.parser import charref

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt (original_text, shift_amount):
    newletter =""
    if direction == "encode":
        for letter in original_text:
            #1st gets first letter's alphabet's list index in [number] format, then shifts the index by desired amount
            shifted_letter = alphabet.index(letter) + shift_amount

            #calculate possible out of range (remainder of letter / lenght of alphabet list) in order to restart from beginning
            shifted_letter %= len(alphabet)

            #adds the processed letter to the newletter string
            newletter += alphabet[shifted_letter]

        print(f"The encoded result is {newletter}")

    else:
        print("Wrong input, please retry !")


encrypt(text, shift)




