from eulerlib import generateNPrimes, timedRun

def euler7():
    """Solves problem 7 of Project Euler."""
    primes = generateNPrimes(10001)
    print("Count = ", len(primes))
    print("Last = ", primes[-1])
    
if __name__ == "__main__":
    timedRun(euler7)
