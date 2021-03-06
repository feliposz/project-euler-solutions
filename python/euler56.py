##Problem 56
##07 November 2003
##
##A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
##
##Considering natural numbers of the form, a^b, where a, b <= 100, what is the maximum digital sum?

highest = 0

for a in range(1, 101):
    for b in range(1, 101):
        n = a ** b
        total = 0
        for c in str(n):
            total += int(c)
        if total > highest:
            print(a, "**", b, "sum of digits is", total)
            highest = total
print("done")
