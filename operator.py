#Simple program using operator %  to check
#if a remainder of a division is even or not.

first_number = (int(input("Number you want to check with operator :")))
dividend_operator = (int(input("Please specify your dividend :")))
perform_operation = first_number % dividend_operator
print (f"The remainder for this division is : {perform_operation}")
if perform_operation  > 0:
    print("The remainder is uneven.")
else:
    print ("The remainder is even.")