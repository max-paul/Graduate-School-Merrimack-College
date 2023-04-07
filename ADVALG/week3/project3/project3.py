"""
Project #3

Create a program that computes the "Tribonacci" sequence numbers
○Unlike the traditional Fibonacci sequence (a number is the sum of the two previous ones), here a number is the sum of the three previous ones (the initial numbers are 1,1,1)

The first 9 elements of the sequence are:
1, 1, 1, 3, 5, 9, 17, 31, 57, …

Your program should asks the user a positive Integer n and the deliver the n-th element of the Tribonacci sequence

For example, for n = 6, it delivers 9
Make sure your program uses Dynamic Programming in an efficient way (for example, keeping in memory previously computed elements)
This program must be your own, do not use someone else’s code
Any specific questions about it, please bring to the Office hours meeting this Monday or contact me by email
This is a challenging program to make sure you are mastering your Python programming skills, as well as your asymptotic analysis understanding
Don’t be shy with your questions

"""
"""
Report / notes
I found this challenge to be fairly simple as we can utilize a list
and call it by its indices. especially when we are given that the list
always starts with [1,1,1] so we dont have to handle the case when
len(list) < 3 


"""



def tribonacci(n):
    # Initialize the first three elements of the sequence
    trib = [1, 1, 1]

    # If n is less than or equal to 3, return the corresponding element
    if n <= 3:
        return trib[n-1]

    # Otherwise, use dynamic programming to compute the n-th element
    for i in range(3, n):
        trib.append(trib[i-1] + trib[i-2] + trib[i-3])

    return trib[n-1]

# Ask the user for input
n = int(input("Enter a positive integer: "))

# Call the tribonacci function and print the result
result = tribonacci(n)
print("The n-th element of the Tribonacci sequence is:", result)


