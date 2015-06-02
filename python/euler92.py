def chainResult(num):
    while num != 1 and num != 89:
        s = str(num)
        num = 0
        for c in s:
            num += int(c) * int(c) 
    return num

count = 0
for num in range(1,10000000):
    if chainResult(num) == 89:
        count += 1 
print(count)
