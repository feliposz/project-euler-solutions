##Problem 32
##06 December 2002
##
##We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
##
##The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
##
##Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
##
##HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Ugly solution! Should probably generate the combinations instead!

products = []

for a in range(1, 1000):
    for b in range(1, 10000):
        prod = a * b
        s = str(prod) + str(a) + str(b)

        #check only if it has exactly 9 digits
        if len(s) != 9:
            continue

        #check for repeated digits
        repeated = False
        for i in range(len(s)):
            if s[i] == '0': #0 is not accepted
                repeated = True
                break
            for j in range(i+1, len(s)):
                if (s[i] == s[j]):
                    repeated = True
                    break
            if repeated:
                break
        if not repeated:
            print(a, "*", b, "=", prod);
            if not prod in products:
                products.append(prod)

print(sum(products))
