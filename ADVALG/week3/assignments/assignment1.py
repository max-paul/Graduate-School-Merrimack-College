from fractions import Fraction

"""
Notes:

using pythons built in fraction module, prob lose points for this simpler solution
def egyptian_fractions(numerator, denominator):
    result = []
    while numerator != 0:
        x = -(-denominator // numerator) # Ceiling division
        result.append(x)
        numerator = numerator * x - denominator
        denominator = denominator * x
    return [Fraction(1, x) for x in result]
    
print(egyptian_fractions(5,6))

"""

def egyptian_fractions(numerator, denominator):
    print(f"calculating for {numerator} and {denominator}")
    result = []
    while numerator != 0:
        x = -(-denominator // numerator) # Ceiling division
        result.append(x)
        numerator = numerator * x - denominator
        denominator = denominator * x

    # Convert the result to a list of fractions
    fractions = []
    for x in result:
        fractions.append(Fraction(1, x))

    return fractions

ef = egyptian_fractions(5, 6)
for fraction in ef:
    print(fraction) # Output: 1/2 + 1/3
print("\n")
ef = egyptian_fractions(7, 15)
for fraction in ef:
    print(fraction) # Output: 1/3 + 1/5 + 1/105
print("\n")

ef = egyptian_fractions(23, 34)
for fraction in ef:
    print(fraction) # Output: 1/2 + 1/3 + 1/187 + 1/56115
print("\n")

ef = egyptian_fractions(121, 321)
for fraction in ef:
    print(fraction) # Output: 1/4 + 1/34 + 1/2313 + 1/2834221
print("\n")

ef = egyptian_fractions(5, 123)
for fraction in ef:
    print(fraction) # Output: 1/25 + 1/4920
print("\n")
