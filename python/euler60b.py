"""Problem 60
02 January 2004

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

# Correct solution, not very slow, but the code is just plain ugly!

# Should reimplement the nested fors as a pretty recursive depth first search

import eulerlib
import pickle

#LIMIT = 100000000

print("Generating primes")
primefile = open("primes_10e8.p", "rb")
primes = pickle.load(primefile)
primefile.close()
primeset = set(primes)
#primeset = pickle.load(open("primeset_10e8.p", "rb"))
#isPrimeTable = pickle.load(open("isPrime_10e8.p", "rb"))

def isPrime(num):
    if num <= primes[-1]:
        return num in primeset # O(1)
    else:
        return eulerlib.isPrime(num) # slower (actually this shouldn't be used given the limit...)

small_primes = list(filter(lambda x: x < 10000, primes))

print("Generating combos")
candidates = set([])
added = False
for p1 in small_primes:
    s1 = str(p1)
    for p2 in small_primes:
        if p2 == p1:
            continue
        s2 = str(p2)
        t1 = int(s1 + s2)
        t2 = int(s2 + s1)
        if isPrime(t1) and isPrime(t2):
            for p3 in small_primes:
                if p3 == p1 or p3 == p2:
                    continue
                s3 = str(p3)
                t3 = int(s1 + s3)
                t4 = int(s3 + s1)
                t5 = int(s2 + s3)
                t6 = int(s3 + s2)
                if isPrime(t3) and isPrime(t4) and isPrime(t5) and isPrime(t6):
                    for p4 in small_primes:
                        if p4 == p1 or p4 == p2 or p4 == p3:
                            continue
                        s4 = str(p4)
                        t7 = int(s1 + s4)
                        t8 = int(s4 + s1)
                        t9 = int(s2 + s4)
                        t10 = int(s4 + s2)
                        t11 = int(s3 + s4)
                        t12 = int(s4 + s3)
                        added = False
                        if isPrime(t7) and isPrime(t8) and isPrime(t9) and isPrime(t10) and isPrime(t11) and isPrime(t12):
                            for p5 in small_primes:
                                if p4 == p1 or p4 == p2 or p4 == p3:
                                    continue
                                s5 = str(p5)
                                t13 = int(s1 + s5)
                                t14 = int(s5 + s1)
                                t15 = int(s2 + s5)
                                t16 = int(s5 + s2)
                                t17 = int(s3 + s5)
                                t18 = int(s5 + s3)
                                t19 = int(s4 + s5)
                                t20 = int(s5 + s4)
                                if isPrime(t13) and isPrime(t14) and isPrime(t15) and isPrime(t16) and isPrime(t17) and isPrime(t18) and isPrime(t19) and isPrime(t20):   
                                    candidates.add((p1, p2, p3, p4, p5))
                                    print(p1, p2, p3, p4, p5)
                                    added = True
                                if added: break # for p5
                        if added: break # for p4
                if added: break # for p3
        if added: break # for p2
            
print(candidates)
            

