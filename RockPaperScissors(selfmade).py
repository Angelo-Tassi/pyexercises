import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choices = ["Rock", "Paper", "Scissors"]
winner = ["Player", "Computer", "Tie"]
computer_choose = random.choice(game_choices)
player_choose = [game_choices]
game_winner =[winner]

#Player choice
while True:

    player_input = input("Please type CAPITAL R for Rock, P for Paper and S for scissors :\n")
    print("Player Choice :")
    if player_input == "R":
        player_choose = game_choices[0]
        print(rock)
        break

    elif player_input == "P":
        player_choose = game_choices[1]
        print(paper)
        break

    elif player_input == "S":
        player_choose = game_choices[2]
        print(scissors)
        break

    else:
        print("Wrong input, please retry.. !")

    continue

#computer choice

print("Computer Choose..")

if computer_choose == game_choices[0]:
    print(rock)

if computer_choose == game_choices[1]:
    print(paper)

if computer_choose == game_choices[2]:
    print(scissors)



#Declaring winner logic


if player_choose == "Rock" and computer_choose == "Scissors":
        winner=winner[0]

if player_choose == "Paper" and computer_choose == "Scissors":
        winner = winner[1]

if player_choose == "Paper" and computer_choose == "Rock":
        winner = winner[0]

if player_choose == "Scissors" and computer_choose == "Rock":
        winner = winner[1]

if player_choose == "Rock" and computer_choose == "Paper":
        winner = winner[1]

if player_choose == "Scissors" and computer_choose == "Paper":
        winner = winner[0]

if player_choose == computer_choose:
        winner = winner[2]




if winner == "Player":
    print(f"Winner is : {winner} ! ")
elif winner == "Computer":
    print(f"Winner is : {winner} ! ")
else:
    print(f"Game is a {winner} !")