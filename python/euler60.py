# FUCKING SLOW - DO THIS IN A DIFFERENT MANNER STUPID!

import eulerlib

LIMIT = 100000000

print("Generating primes")
primes, isPrimeTable = eulerlib.generatePrimesSieve(LIMIT)

def isPrime(num):
    if num < LIMIT:
        return isPrimeTable[num]
    else:
        return eulerlib.isPrime(num)


def filterCombos(num, elements):
    candidates = []
    for e in elements:
        combo1 = int(str(num) + str(e))
        combo2 = int(str(e) + str(num))
        if isPrime(combo1) and isPrime(combo2):
            candidates.append(e)
    return candidates

def checkCombo(elements):
    for i in elements:
        for j in elements:
            if i != j:
                p1 = int(str(i) + str(j))
                p2 = int(str(j) + str(i))
                if not isPrime(p1) or not isPrime(p2):
                    return False
    return True

def combinations(elements, expected_size, level=0):
    #print("combinations", elements)
    if len(elements) < 2:
        return []
    for i in range(len(elements)):
        if level == 0: print("Testing =", elements[i])
        candidates = [elements[i]]
        for j in range(i+1, len(elements)):
            num1 = int(str(elements[i]) + str(elements[j]))
            num2 = int(str(elements[j]) + str(elements[i]))
            if isPrime(num1) and isPrime(num2):
                candidates.append(elements[j])
        candidates = combinations(candidates, expected_size, level + 1)
        if len(candidates) == expected_size:
            return candidates
        elif level > 0:
            return []
    return None

##print("Generating combinations")
##candidates = combinations(primes[:100], 4)

def discarded():
    print(len(primes))

    print("Generating candidates table")
    candidates = {}
    for i in range(LIMIT):
        for j in range(i+1, LIMIT):
            pi = primes[i]
            pj = primes[j]
            num1 = int(str(pi) + str(pj))
            num2 = int(str(pj) + str(pi))
            if isPrime(num1) and isPrime(num2):
                candidates[pi] = candidates.get(pi, set([]))
                candidates[pi].add(pj)
                candidates[pj] = candidates.get(pj, set([]))
                candidates[pj].add(pi)

    print(len(candidates))


    print("Checking candidates pairing")
    for i in candidates:
        for j in candidates:
            if i in candidates[j] and len(candidates[i] & candidates[j]) > 1:
                print(i, j, candidates[i] & candidates[j])
            
        if len(candidates[k]) >= 2:
            print(k, candidates[k])
            
        if len(candidates[num]) > 1:
            print(num, candidates[num])

    primeCount = {}
    for elements in candidates:
        for num in candidates[elements]:
            primeCount[num] = primeCount.get(num, 0) + 1

    for num in primeCount:
        if primeCount[num] > 1:
            print(num)
           


def discarded2():
    print("Generating combos")
    combos = {}
    for p in primes:
        sp = str(p)
        if len(sp) < 2:
            continue
        for i in range(1, len(sp)):
            n1 = int(sp[:i])
            n2 = int(sp[i:])
            rev = int(sp[i:] + sp[:i])
            if isPrime(n1) and isPrime(n2) and isPrime(rev):
                combos[n1] = combos.get(n1, set([n1]))
                combos[n1].add(n2)
    print(len(combos))

    print("Filtering combos")
    filtered = []
    for a in combos:
        for b in combos:
            c = combos[a] & combos[b]
            if len(c) == 5 and checkCombo(c):
                filtered.append(c)

    print(len(filtered))

    print("Findind smallest sum")
    smallest = sum(filtered[0])
    smallest_combo = filtered[0]
    for c in filtered:
        s = sum(c)
        if s < smallest:
            smallest = s       
    print("Smallest sum = ", smallest, sorted(smallest_combo))

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
                            candidates.add((p1, p2, p3, p4))
                            added = True
                        if added: break
                    if added: break
                if added: break
            if added: break
            

            

