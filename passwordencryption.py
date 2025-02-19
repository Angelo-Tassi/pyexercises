

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, switch):
        cipher_text = ""

        if switch == "encode":
            #ENCRYPT

            for letter in original_text:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")

        if  switch == "decode":
            #DECRYPT

            for letter in original_text:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the decoded result: {cipher_text}")





while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:  # Validate input
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue  # Skip the rest of the loop and ask again

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, switch=direction)


    # Ask the user if they want to continue
    restart = input("Do you want to go again? (yes/no):\n").lower()
    if restart != "yes":
        break  # Exit the loop if the user doesn't want to continue

