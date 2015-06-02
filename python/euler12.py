# I found this great prime generator at:
#   http://stackoverflow.com/a/568618

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

# -------------------------------------------------------
# My solution starts here
#
# Example:
#   120 = 2^3 * 3^1 * 5^1
# So the divisors are necessarily in the form:
#   2^x * 3^y * 5^z
# Possible values are:
#   x=0,1,2,3 y=0,1 z=0,1
# Thus, the number of combinations is:
#   4*2*2 = 16

primes_gen = gen_primes()
primes = [next(primes_gen), ] # keep primes in a list

# Not sure if this is a great way to factorate
def factorate(num):
    factors = {}
    for p in primes:
        if (primes[-1] < num): # generate only as many primes as necessary
            primes.append(next(primes_gen))
        while (num % p) == 0:
            num /= p
            factors[p] = factors.get(p, 0) + 1
        if num == 1:
            break
    return factors

from datetime import datetime

start = datetime.now()
i = 1
triangle = 0
max_count = 0
while (True):
    triangle += i
    i += 1
    factors = factorate(triangle)
    count = 1
    for x in factors.values():
        count *= (x + 1)
    if count > max_count:
        max_count = count
        print("i =", i, " number =", triangle, " divisors =", count)
    if count > 500: break
print(datetime.now() - start)
# took under 18s in my machine
