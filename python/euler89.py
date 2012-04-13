"""Problem 89
18 February 2005
http://projecteuler.net/problem=89

The rules for writing Roman numerals allow for many ways of writing
each number (see About Roman Numerals...). However, there is always a
"best" way of writing a particular number.

For example, the following represent all of the legitimate ways of
writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the
least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target
As...'), contains one thousand numbers written in valid, but not
necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see About Roman
Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain
no more than four consecutive identical units.
"""

from eulerlib import timedRun

# Dictionary of values for converting from roman to decimal
letterValue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
               "M": 1000}

# Dictionary of values for converting from decimal to roman
valueLetter = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
               50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM",
               1000: "M"}

# Check this for detailed rules for roman conversions:
# http://projecteuler.net/about=roman_numerals

def euler89():
    """Solves problem 89 from Project Euler."""
    total = 0
    file = open("roman.txt")
    while True:
        roman = file.readline()
        if not roman:
            break
        roman = roman.strip()
        value = roman2decimal(roman)
        proper = decimal2roman(value)
        saved = len(roman) - len(proper)
        total += saved
    file.close()
    print(total)

def roman2decimal(roman):
    """Convert any properly formed roman number to its decimal value.

    The result is undefined for ill formed roman numbers."""
    
    value = 0
    for i in range(len(roman)):
        num = letterValue[roman[i]]
        # If next letter value is bigger, invert sign
        # E.g.: IX = -1 + 10 = 9
        if i < len(roman) - 1 and letterValue[roman[i + 1]] > num:
            num = -num;
        value += num
    return value
    
def decimal2roman(value):
    """Returns a number represented in proper roman digits."""
    roman = ""
    for num in sorted(valueLetter, reverse=True):
        while value >= num:
            roman += valueLetter[num]
            value -= num
    return roman

assert roman2decimal("I") == 1, "expected value for I is 1"
assert roman2decimal("V") == 5, "expected value for V is 5"
assert roman2decimal("X") == 10, "expected value for X is 10"
assert roman2decimal("L") == 50, "expected value for L is 50"
assert roman2decimal("C") == 100, "expected value for C is 100"
assert roman2decimal("D") == 500, "expected value for D is 500"
assert roman2decimal("M") == 1000, "expected value for M is 1000"

assert roman2decimal("IIII") == 4, "expected value for IIII is 4"
assert roman2decimal("MMMM") == 4000, "expected value for MMMM is 4000"
assert roman2decimal("IM") == 999, "expected value for IM is 999"
assert roman2decimal("MI") == 1001, "expected value for MI is 1001"
assert roman2decimal("IX") == 9, "expected value for IX is 9"
assert roman2decimal("CDD") == 900, "expected value for CDD is 900"

assert decimal2roman(1) == "I", "expected value for 1 is I"
assert decimal2roman(4) == "IV", "expected value for 4 is IV"
assert decimal2roman(5) == "V", "expected value for 5 is V"
assert decimal2roman(9) == "IX", "expected value for 9 is IX"
assert decimal2roman(10) == "X", "expected value for 10 is X"
assert decimal2roman(40) == "XL", "expected value for 40 is XL"
assert decimal2roman(50) == "L", "expected value for 50 is L"
assert decimal2roman(90) == "XC", "expected value for 90 is XC"
assert decimal2roman(100) == "C", "expected value for 100 is C"
assert decimal2roman(400) == "CD", "expected value for 400 is CD"
assert decimal2roman(500) == "D", "expected value for 500 is D"
assert decimal2roman(900) == "CM", "expected value for 900 is CM"
assert decimal2roman(1000) == "M", "expected value for 1000 is M"

test = {99: "XCIX", 42: "XLII", 32: "XXXII", 2012: "MMXII", 1981: "MCMLXXXI"}
for t in test:
    s = "expected value for " + str(t) + " is " + test[t]
    assert decimal2roman(t) == test[t], s

for n in range(1, 5000):
    s = "unepected conversion for " + str(n)
    assert n == roman2decimal(decimal2roman(n)), s

if __name__ == "__main__":
    timedRun(euler89)
