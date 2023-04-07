"""
Implement a recursive program that asks the number of disks and delivers the minimal number of moves to solve the Towers of Hanoi efficiently
Your program must have a recursive function that delivers the number of movements for a given number of disks

"""

def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1

n = int(input("Enter the number of disks: "))
print("The minimal number of moves required is:", hanoi(n))