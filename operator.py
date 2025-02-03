#Simple program using modulo operator %  to check if a number is odd or even

first_number = (int(input("Number you want to check with modulo operator :")))
print ("Let's check if this number can be perfectly divided by 2...")
perform_operation = first_number % 2
print (f"The remainder for this division is : {perform_operation}")
if perform_operation  > 0:
    print("The number is odd.")
else:
    print ("The number is even.")