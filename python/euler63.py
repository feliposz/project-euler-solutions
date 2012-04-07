"""Problem 63
13 February 2004

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def euler63():
    count = 0
    for base in range(1,1000):
        for expt in range(1,1000):
            num = base ** expt
            length = len(str(num))
            if length == expt:
                count += 1
            elif length > expt:
                break
    print(count)

if __name__ == "__main__":
    euler63()
