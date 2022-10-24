from swapElements import Swap

def main():

    s = Swap()
    s.getLen()
    s.createVector()
    print("Original List", s.vector)
    new = s.swapPositions()
    print("Swapped List", new)
    return


if __name__ == "__main__":
    main()
