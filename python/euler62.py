"""Problem 62
30 January 2004

The cube, 41063625 (345³), can be permuted to produce two other cubes:
56623104 (384³) and 66430125 (405³). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its
digits are cube.

"""

cubes = {}
base = {}

i = 1
while True:
    num = i ** 3
    index = "".join(sorted(list(str(num))))
    cubes[index] = cubes.get(index, 0) + 1
    base[index] = base.get(index, i)
    if cubes[index] == 5:
        print("Base =", base[index], "Cube =", base[index]**3)
        break
    i += 1
