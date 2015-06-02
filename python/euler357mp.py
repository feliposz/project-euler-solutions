"""Prime generating integers
Problem 357
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

# Multiprocessing version!!!!!

from eulerlib import generatePrimesSieve
import multiprocessing

def isPrimeGeneratingInteger(n):
    global isPrime
    if n > 10 and not n%10 in (0, 2, 8):
        return False
    for d in range(1, n+1):
        if n % d != 0:
            continue
        nd = n // d
        if d > nd:
            break
        x = d + n // d
        #print(d, "+", n, "/", d, "=", d, "+", n // d, "=",x)
        if not isPrime[x]:
            return False
    return True

def solvePartial(start, end, out_q):
    total = 0
    for i in range(start, end+1):
        if isPrimeGeneratingInteger(i):
            print(i)
            total += i
    out_q.put(total);

if __name__ == '__main__':

    LIMIT = 1000
    #LIMIT = 100000000

    print("Generating primes... ", end="")
    primes, isPrime = generatePrimesSieve(LIMIT+2)
    print("done.")

    procs = []
    nprocs = 1
    for i in range(nprocs):

        # calc the range to pass for the given process
        start = (LIMIT // nprocs) * i + 1
        end = (LIMIT // nprocs) * (i+1)
        if i == nprocs - 1:
            end = LIMIT

        # create a child process
        print("process", i, start, end)
        out_q = multiprocessing.Queue()
        p = multiprocessing.Process(target=solvePartial, args=(start, end, out_q))
        procs.append(p)
        p.start()

    total = 0
    for i in range(nprocs):
        total += out_q.get()

    for p in procs:
        p.join()

    print("soluction: ", total)


