import math
import time
from eulerlib import isPrime, generateStringPermutations

def euler41():
    largest = 0
    for n in range(3,11):
        print("Generating permutations for n = ", n, end="")
        perms = generateStringPermutations(
            "".join([str(i) for i in range(1, n)]))
        print("...done.")
        print("Checking primes...")
        for p in perms:
            num = int(p)
            if isPrime(num):
                #print(num)
                largest = max(largest, num)
        print("done.")
    print("Largest prime found =", largest)
    
if __name__ == "__main__":
    euler41()
