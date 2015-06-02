from functools import reduce

def euler16():
    """Solves problem 16 of Project Euler."""
    # 'normal' way
    total = 0
    for c in str(2**1000):
        total += int(c)
    print(total)

    # functional way 1
    print(reduce(lambda x, y: x + y, [int(i) for i in str(2**1000)]))
    
    # functional way 2
    print(sum([int(i) for i in str(2**1000)]))

if __name__ == "__main__":
    euler16()
    
