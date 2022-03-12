memo = [False] * 10000000

def sum_digit_groups(num):
    if num >= 10 and num < len(memo):
        if memo[num]:
            return memo[num]
    result = []
    divisor = 10
    while divisor < num:
        for m in sum_digit_groups(num % divisor):
            result.append(num // divisor + m)
        divisor *= 10
    result.append(num)
    if num >= 10 and num < len(memo):
        memo[num] = result
    return result

def is_s_number(num):
    sq = num * num
    sss = set(sum_digit_groups(sq))
    return num in sss

t = 0

for x in range(2, 1000000+1):
    if is_s_number(x):
        t += x*x

print(t)

# 100 => 41333 ok
# 1000000 => 128088830547982 ok
