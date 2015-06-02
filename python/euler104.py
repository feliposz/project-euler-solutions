from eulerlib import timedRun

def isPandigital(s):
    for c in "123456789":
        if not c in s:
            return False
    return True


def euler104():
    k = 1
    a = 1 # Fib 1
    b = 1 # Fib 2

    while True:
        c = a + b
        a = b
        b = c
        k += 1
        lastDigits = a % 1000000000
        if isPandigital(str(lastDigits)):
            print(k)
            firstDigits = str(a)[:9]
            if isPandigital(firstDigits):
                print("^^^^^^ Found!")
                break

if __name__ == "__main__":
    timedRun(euler104)
