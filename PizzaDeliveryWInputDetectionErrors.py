#Start

print("Welcome to Python Pizza Deliveries!")

#Define bill

bill = 0

#get the size
while True:
    size = input("What size pizza do you want? press capital S, M or L: ")
    if size == "S":
        bill =(int(11))
        break
    elif size == "M":
        bill = (int(15))
        break
    elif size == "L":
        bill = (int(25))
        break
    else : print ("Wrong input, please retry ..")
    continue

#pepperoni option

while True:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "N":
        bill = bill
        break
    elif pepperoni == "Y":
        bill += 2
        break
    else: print ("Wrong input, please retry .. we need to know if you want pepperoni on pizza NOW !")
    continue

#extra cheese

while True:
    cheese = input("Do you want extra cheese on your pizza? Y or N: ")
    if cheese == "N":
        bill = bill
        break
    elif cheese == "Y":
        bill += 1
        break
    else: print ("Wrong input, please retry .. we need to know if you want EXTRA cheese on pizza RIGHT NOW !")
    continue

#Total

print(f"Your total bill is {bill} $ , NOW GTFO of HERE !")