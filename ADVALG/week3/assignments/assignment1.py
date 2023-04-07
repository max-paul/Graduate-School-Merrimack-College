from fractions import Fraction

"""
Notes:

Hoping I dont lose points for using the built in fractions package.. only used for formatting the print statement


This was a fun task and a cool mathmatical solution. Satisfying to understand and watch!!

Cool facts from some research...
Egyptian Fractions are a way of representing a positive rational number as a sum of distinct unit fractions.
Egyptian Fractions have applications in diverse fields such as computer science, cryptography, and music theory.
Egyptian Fractions have interesting properties, such as always having a finite number of terms in their expansion.


I find the fact that the optimal Egyptian Fraction representation unsolved problem in mathematics.
"""

def egyptian_fractions(numerator, denominator):
    result = [] # Initialize an empty list to hold the output fractions
    while numerator != 0: # Continue until we have expressed the entire number as unit fractions
        x = -(-denominator // numerator) # Calculate the next unit fraction by taking the ceiling of the division between the denominator and the numerator
        result.append(x) # Add the new unit fraction to the list of results
        numerator = numerator * x - denominator # Update the numerator by subtracting the corresponding fraction
        denominator = denominator * x # Update the denominator by multiplying by the same factor
    return [Fraction(1, x) for x in result] # Convert the list of unit fractions to a list of proper fractions (Fractions library used here)



print("for 5/6")
print(egyptian_fractions(5,6))
print("\n")
print("for 7/15")
print(egyptian_fractions(7, 15))
print("\n")
print("for 23/34")
print(egyptian_fractions(23, 34))
print("\n")
print("for 121/321")
print(egyptian_fractions(121, 321))
print("\n")
print("for 5/123")
print(egyptian_fractions(5, 123))
print("\n")

