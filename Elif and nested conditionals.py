
#Rollercoaster security check
#Elif and conditionals Nesting

print("Welcome to the rollercoaster ! We need to ask you some questions concerning security ..")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    #check price

    if age <= 12:
        bill = 8
        print (f"Ticket price for {age} year olds is 8$")
    elif age <= 18 :
        bill = 12
        print (f"Ticket price for {age} year olds is 12$")
    else:
        bill =19
        print ("Ticket price for people that is over 18 years old is 19$")

    #check if the person wants a picture of the ride

    wants_photo = input("Do you want a picture taken? Type y for Yes and n for No :")
    if wants_photo == "y":
            bill += 3
            print(f"Ok, we include the picture, so the total cost of the ride is: {bill}$")
    else:
        print (f"Ok , we wont charge the photo, so the total cost of the ride is still {bill}$.")


elif height < 120 and age > 18:
    print ("We can't sell you a ticket; ")
    if age > 18 and height < 120:
        print("We are very sorry, even if you are an adult, for security reasons, you must be over 120cm to ride")
else:
    print("Sorry you have to grow taller before you can ride.")