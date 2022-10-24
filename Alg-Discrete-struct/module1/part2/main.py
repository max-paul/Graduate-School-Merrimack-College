from zigzag import ZigZag


def main():
    """
    Our main logic loop for runningthe main program
    :return: None
    """
    a = int(input("Enter item A: "))
    b = int(input("Enter item B: "))
    c = int(input("Enter item C: "))
    zig = ZigZag(a, b, c)
    zig.checkZigZag()
    print(zig.getResult())
    return


if __name__ == "__main__":
    main()
