from linkedList import LinkedList

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
    mylist = LinkedList()
    # we know the list is sorted, brute set the initial linked list
    for i in reversed(nums):
        mylist.insertBeginning(i)

    # for each item we entered into the linked list, lets check
    mylist.printList("List Prior to operations")


    loop = True
    while loop:
        """
        Continuously prompt the user to enter an integer
        """
        try:
            user_input = eval(input("Please enter an integer :) "))
            loop = False
        except:
            print("Please enter a string")

    for i in nums:
        """
        For each item we passed into the txt file
        
        get the current Node, and the value of the Next,
        if node value == user_input then remove value from LL
        if node values != user_input then lets add this new value BUT
        keep integrity of linked list order :)
        """
        mylist.nextCurrent()
        current_data = mylist.Current.Data
        try:
            next_data = mylist.Current.Next.Data
        except:
            next_data = None

        if user_input == next_data:
            print(f"Found {user_input} in the Linked List")
            print(f"Removing Value {user_input}")
            mylist.removeCurrentNext()

        if user_input > current_data and \
                (user_input < next_data if next_data is not None else 9999999999999999999):
            """
            if user input is greater than current data AND
            user input is greater than next data
            
            Handling if the Next value is None i.e end of LL,
            hard coded 9999999999999999999 (so if a value we are entering is greater than the max,
            im assuming an item in our list will be less than 9999999999999999999 as the next value
            """
            print(f"Did Not Find {user_input} in the Linked List")
            print(f"Adding Value {user_input}, Between {current_data} and {next_data}")
            mylist.insertCurrentNext(user_input)
        elif user_input < current_data == nums[0]:
            """
            Handling insertion at index 0
            
            if user input is less than the current value AND 
            the current value is equal to the lowest item in our list (Index 0 as its a sorted list)
            """
            mylist.insertBeginning(user_input)
        elif user_input == current_data and current_data == nums[0]:
            mylist.removeBeginning()

    #mylist.resetCurrent()
    mylist.printList("List after Operations")

if __name__ == "__main__":
    main()
