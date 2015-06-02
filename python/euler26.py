# NOTE:
# it appears I could cut some corners here, but i wanted to generate
# the full numbers to check this is working

# checkRecurringCycle(divisor: int): int
#
# This function finds the size of a recurring cycle for 1 / divisor
# Ex: 1 / 3 = 0.(3)33333 only 1
# Ex: 1 / 7 = 0.(142857)142857... size is 6

def checkRecurringCycle(divisor):
    
    assert divisor > 0, "Divisor must be greater than 0"
    assert type(divisor) == type(1), "Divisor must be an integer"
    
    cycle = "" # this is only used for debugging. It's what is after "0."
    count = 0
    remainder = 10
    # (actually 1, but since divisor > 1,
    #  start with 10 and "0." for the quotient)
    remainders = [] # keep a list of all the remainders
    
    while remainder != 0:
        
        remainders.append(remainder)
        
        if remainder < divisor: # can't divide
            cycle += "0" # insert a zero in the decimal place
            remainder *= 10 # and add a zero to the remainder
        else:
            cycle += str(remainder // divisor)
            remainder = remainder % divisor * 10        
        count += 1

        # if the remainder is repeated, then we reached the end of the cycle
        if remainder in remainders:
            cycle += "..."
            break

    print("0." + cycle)

    if remainder != 0:
        # cycle starts at the first repeated remainder
        return count - remainders.index(remainder)
    else:
        # number is exact
        return 0

# This finds the largest recurring cycles for 1/d for d<MAX
# TODO: check only for primes! Especially if MAX > 1000
high = 0
num = 0
MAX = 100
for i in range(1, MAX):
    size = checkRecurringCycle(i)
    if (size > high):
        high = size
        num = i
print("num =", num, "recurring cycle size = ", high)
