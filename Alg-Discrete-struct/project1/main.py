from linkedList import LinkedList
import sys
def readFile():
    """
    our operational method for reading in the txt file!

    :return: list of nums from txt file
    """
    nums = []
    file = open("data.txt", "r")
    for i in file:
        nums.append(int(i.strip("\n")))
    nums.sort()
    return nums


def main():
    """
    Our main loop to handle the linked list operations

    :return: None
    """
    # reading in the file data
    nums = readFile()
    # starting out linkedList
    L = LinkedList()
    # we know the list is sorted, brute set the initial linked list
    for i in reversed(nums):
        L.insertBeginning(i)

    # for each item we entered into the linked list, lets check
    L.printList("List Prior to operations")


    loop = True
    while loop:
        """
        Continuously prompt the user to enter an integer
        """
        try:
            x = eval(input("Please enter an integer :) "))
            loop = False
        except:
            print("Please enter a string")

    for i in nums:
        """
        For each item we passed into the txt file
        
        get the current Node, and the value of the Next,
        if node value == x then remove value from LL
        if node values != x then lets add this new value BUT
        keep integrity of linked list order :)
        """
        L.nextCurrent()
        current_data = L.Current.Data
        try:
            next_data = L.Current.Next.Data
        except:
            next_data = None

        if x == next_data:
            print(f"Found {x} in the Linked List")
            print(f"Removing Value {x}")
            L.removeCurrentNext()

        if x > current_data and \
                (x < next_data if next_data is not None else sys.maxsize):
            """
            if user input is greater than current data AND
            user input is greater than next data
            
            Handling if the Next value is None i.e end of LL,
            hard coded sys.maxsize (so if a value we are entering is greater than the max,
            im assuming an item in our list will be less than sys.maxsize as the next value
            sys.maxsize is the maximum size a data struct may by in python: 9223372036854775807
            """
            print(f"Did Not Find {x} in the Linked List")
            print(f"Adding Value {x}, Between {current_data} and {next_data}")
            L.insertCurrentNext(x)
        elif x < current_data == nums[0]:
            """
            Handling insertion at index 0
            
            if user input is less than the current value AND 
            the current value is equal to the lowest item in our list (Index 0 as its a sorted list)
            """
            L.insertBeginning(x)
        elif x == current_data and current_data == nums[0]:
            """
            if user input == current data
            and current data is equal to the lowest item in the sorted list
            lets remove the first item
            """
            L.removeBeginning()

    L.printList("List after Operations")

if __name__ == "__main__":
    main()
