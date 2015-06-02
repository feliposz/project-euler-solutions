from random import randint

def testMillerRabin(n, k):
    """Return False if n is a composite. Return True if n is probably a prime."""
    assert n > 3
    assert k > 0
    
    d = n - 1
    s = 0
    while (d % 2 == 0):
        s += 1
        d //= 2
    print("n =", n, " => ", n-1,"= 2 **", s, "*", d)

    for repeat in range(k):
        print("repeat =", repeat, "/", k)
        a = randint(2, n-2)
        x = (a ** d) % n
        print("a =", a, " x =", x)
        if x == 1 or x == n - 1:
            continue
        nextLoop = False
        for r in range(1, s):
            x = (x*x) % n
            print("r =", r, " x=", x)
            if x == 1:
                return False
            if x == n - 1:
                nextLoop = True
                break
        if nextLoop:
            continue
        return False
    return True

testMillerRabin(999999991, 3)
