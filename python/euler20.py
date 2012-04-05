from math import factorial
from eulerlib import sumDigits

def euler20():
    """Solves problem 20 of Project Euler."""
    print(sumDigits(factorial(100)))

if __name__ == "__main__":
    euler20()
