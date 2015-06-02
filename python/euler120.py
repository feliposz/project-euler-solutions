"""Problem 120
21 April 2006

Let r be the remainder when (a-1)^n + (a+1)^n is divided by a².

For example, if a = 7 and n = 3, then r = 42: 6³ + 8³ = 728 = 42 mod
49. And as n varies, so too will r, but for a = 7 it turns out that
rmax = 42.

For 3 <=  a <= 1000, findsum(rmax).

"""

# kind of slow, but correct

sum_r_max = 0
for a in range(3, 1001):
    print(a)
    r_max = 0
    n = 0
    while True:
        r = ((a - 1) ** n + (a + 1) ** n) % (a * a)
        if r > r_max:
            r_max = r
            count = 1
        if r == r_max:
            count += 1
            if count == 3:
                break
        n += 1
    sum_r_max += r_max

print(sum_r_max)
