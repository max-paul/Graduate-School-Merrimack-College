from Person import Person
from Stack import Stack
from utils import validateInput
import csv


def main():
    """
    Our main loop

    Reads the CSV file person.csv
    puts each row into a person object
    and then pushes the person into the stack!

    Prompt the user to enter a number 1-4, pop that many then print the top of the stack
    :return: Nothing
    """
    myStack = Stack()
    with open("./person.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            newPerson = Person(row[0], row[1], row[2])
            myStack.push(newPerson)

    while not myStack.empty():
        valid = True
        while valid:
            inp = eval(input("Please enter a number between 1-4: "))
            valid = validateInput(inp)
            if valid:
                print("Invalid Choice, Please enter a number between 1-4")

        for i in range(0, inp, 1):
            myStack.pop()

        print(f"After popping {inp} variables, the current stack size is: {myStack.size()}")
        if myStack.empty():
            print("The stack is empty")
        else:
            print(f"The top of the stack contains: {myStack.peek().__dict__}")


if __name__ == "__main__":
    main()
