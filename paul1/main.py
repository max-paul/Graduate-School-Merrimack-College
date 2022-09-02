'''
The circumference of a circle with a radius of 2.750 is 17.27875

The area of a circle with a radius of 2.750 is 23.75827

The volume of a sphere with a radius of 2.750 is 87.11367
'''
from circle import Circle

loop = 'y'
while loop.lower() == 'y':
    try:
        radius = float(input("Please enter any number great than 0: "))
        shape = Circle(radius)
        print(f"The area of the a circle with the radius of {Circle(radius).radius} is {shape.area()}")
        print(f"The circumference of the a circle with the radius of {Circle(radius).radius} is {shape.circumference()}")
        print(f"The volume of the a circle with the radius of {Circle(radius).radius} is {shape.volume()}")

        loop = input("Would you like to try again? Enter (Y)es to continue:")

    except ValueError:
        print("You have entered a non number value for the radius")


'''
output from a radius of 2.75

Please enter any number great than 0: 2.75
The area of the a circle with the radius of 2.75 is 23.75829444277281
The circumference of the a circle with the radius of 2.75 is 17.27875959474386
The volume of the a circle with the radius of 2.75 is 87.11374629016697
Would you like to try again? Enter (Y)es to continue:n

Process finished with exit code 0



unit test output: 
/usr/local/bin/python3.10 /Users/max/Documents/GitHub/Graduate-School-Merrimack-College/paul1/unitTest.py 
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

Process finished with exit code 0
'''