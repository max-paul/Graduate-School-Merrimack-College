from remainder import Remainder


# starting while loop to keep asking for input if its a non-positive integers
while True:
    # try block for exception handling
    try:
        num1 = int(input("Enter the first value: "))
        num2 = int(input("Enter the second value: "))
        # if either of the inputs are less than 0 raise the Value Error defined below
        if num1 < 0 or num2 < 0:
            raise ValueError
        # send the numbers into the class and get the results
        remainder = Remainder(num1, num2)
        #displaying the results and the boolean result
        print(f"Is the remainder for {num1} and {num2} 0?: {remainder.value}")
        # break as we successfully completed the run
        if remainder.value == False:
            continue
        else:
            break
    # defining value error and continuing to give the user another chance to submit values
    except ValueError:
        print("we must enter positive integers only :) ")
        continue

