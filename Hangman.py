import random


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
#HIDDEN WORD

#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"

#Setting lives, logic to keep looping
# and container list out of the loop to save guessed letters to reprint.

player_lives = 6
game_over = False
correct_letters = []



while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        #REPRINT LETTERS OUTSIDE THE LOOP

        elif letter in correct_letters:
                display += letter

        else:
            display += "_"






    print("Your situation :")
    print(display)

    #  If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    #   print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.


    #LOOSING LIVES:

    #INSTRUCTOR VERSION:
    #if guess not in chosen_word
    #player_lives -= 1

    #I CAME UP WITH
    if guess not in correct_letters:
        player_lives -= 1

    #INSTRUCTOR VERSION TO PRINT ART
    print (stages[player_lives])

    #MY LONG A** VERSION TO PRINT ART

    # if  player_lives == 6:
    #         print(stages[6])
    # if player_lives == 5:
    #         print(stages[5])
    # if player_lives == 4:
    #         print(stages[4])
    # if player_lives == 3:
    #         print(stages[3])
    # if player_lives == 2:
    #         print(stages[2])
    # if player_lives == 1:
    #         print(stages[1])

    print(f"You have {player_lives} lives left !")

    #All lives lost

    if player_lives == 0:
            print("You Loose !")
            game_over=True

    #Guessed all letters win

    if "_" not in display:
        game_over = True
        print("You win.")


