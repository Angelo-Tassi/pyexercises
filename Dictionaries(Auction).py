price ={} #empty dictionary

while True:

    username = (str(input("What is your name ?\n"))).title()
    bid = (int(input("How much do you want to bid ?\n")))

    price[username]=bid #dictionary[key]=value

    newbidder =(str(input("There ar other bidders ? Type yes/no\n"))).lower()
    if newbidder == "yes":
            print("\n" * 20)
            continue
    else: break



def auction_biddings(bidders):#calls the dictionary {price]
    winner=""
    highest_bid=0
    for bidder in bidders: #will loop just keys
        bid_amount = bidders[bidder] #sets the bid amount to key=value
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder #key will fetch the name

    print(f"Goes to {winner} with {highest_bid} $ bid.")
auction_biddings(price)#pass dictionary to function