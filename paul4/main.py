from Rectangle import Rectangle, Parallelepipede


try:
    # get the length
    length = float(input("Enter the Length: "))
    # make surevalue is over 0
    if length < 0:
        raise ValueError
    # Get the width
    width = float(input("Enter the Width: "))
    # make surevalue is over 0
    if width < 0:
        raise ValueError

    # initialize class with length and width
    rec = Rectangle(length,width)
    # call display function
    rec.display()

    # get height input for volume
    height = float(input("Enter the Height: "))
    # check if height is over 0
    if height < 0:
        raise ValueError

    # calc volume
    para = Parallelepipede(length,width,height)

    print(f"The volume of {length} x {width} x {height} = {para.volume()}")
# our value error
except ValueError:
    print("Value must be a number")