def main():
    print("This program computes the square of an integer")
    print()
    n = int(eval(input("Enter an integer: ")))
    acc = 0
    odd = 1
    for i in range(n):
        acc+=odd
        odd+=2
    print("the square of", n, "is", acc)