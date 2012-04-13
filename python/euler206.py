"""Problem 206
06 September 2008

Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each “_” is a single digit.
"""

from eulerlib import timedRun

lowerLimit = 1010101010 # aproximation to sqrt of 1020304050607080900
upperLimit = 1389026623 # aproximation to sqrt of 1929394959697989990

def euler206():
    """Solves problem 206 from Project Euler."""
    mask = "1_2_3_4_5_6_7_8_9_0"
    
    # Only numbers ending in 0 are possible (check lowerLimit!)
    for n in range(lowerLimit, upperLimit, 10):
        
        # To generate a square ending in 900, the last two digits of n
        # must be 30 (...900) or 70 (...4900). Checking this first
        # makes the problem 5 times smaller!
        if not n % 100 in (30, 70):
            continue
        
        s = str(n * n)
        found = True
        for i in range(10):
            if s[i+i] != mask[i+i]:
                found = False
                break
        if found:
            print("Found =", n, s)
            break

if __name__ == "__main__":
    timedRun(euler206)



