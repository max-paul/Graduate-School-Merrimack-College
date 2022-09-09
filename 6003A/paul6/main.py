'''
Written by Max Paul
Merrimack College 6003A
Professor GK
'''

# import our class
from deque import Deque

#initialize our while loop
loop = True
# initialize our class Deque
deq = Deque()

#whle loop is tru
while True:
    # if the Deque is NOT empty go into this block
    if deq.items:
        # prompt user to enter one of the values
        frontOrBack = input("{1} Put item to the front of the Deque "
                            "{2} puts an item at the end of the deque "
                            "{N} to end program: ")
        # if its N or n end the program
        if frontOrBack.lower() == 'n' or frontOrBack.upper() == 'N':
            loop = False

        # if we dont end ask user for data to add to Deque
        itemToAdd = input("Enter Item you would like to add: ")

        # logic to decide where to add data
        if frontOrBack == "1":
            deq.addFront(itemToAdd)
            deq.showQue()
        elif frontOrBack == "2":
            deq.addBack(itemToAdd)
            deq.showQue()
        # if the value is not 1 or 2 or N or n ask the user to input again
        else:
            print("Must enter value 1 or 2.")
            continue
    # if the Deque IS empty then go here
    elif not deq.items:
        # ask what you would like to start the que with
        start = input("enter an item to start the Deque{ enter N to end }: ")
        if start.lower() == 'n' or start.upper() == 'N':
            loop = False
        deq.addBack(start)
        deq.showQue()




