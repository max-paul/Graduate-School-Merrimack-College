"""
Author: Max Paul
Module 1 part 1
October 24, 2022

Is it cold in canada today?
"""

from CanadaCold import CanadianCold
from Temp import Temperature

def main():
    """
    Our main run loop for this module

    We set the canadian temp threshold via input,
    then we set todays temp in F, convert F to C and compare
    :return: None
    """

    # set canadian cold
    canadian_temperatue = CanadianCold()
    # set threshold
    canadian_temperatue.setThresholdC()

    # initiate F class
    f_temperatute = Temperature(canadian_temperatue.getThresholdC())
    # set F from input
    f_temperatute.setF()
    # check if cold
    result = f_temperatute.isCold()
    print("Output: ", result)


if __name__ == "__main__":
    main()
