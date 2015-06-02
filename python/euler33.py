##Problem 33
##20 December 2002
##
##Discover all the fractions with an unorthodox cancelling method.
##
##The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
##
##We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
##
##There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
##
##If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# Eu não entendi esse problema!

# Sem querer, descobri que as frações são:
# 16/64=1/4
# 19/95=1/5
# 26/65=2/5
# 49/98=4/8
# Cujo produto é:
#>>> (16/64)*(19/95)*(26/65)*(49/98)
#0.010000000000000002
# ou:
#>>> (1/4)*(1/5)*(2/5)*(4/8)
#0.010000000000000002
# Que é 1/100, logo a resposta é 100

def cancel_9s(num):
    while num >= 10:
        num = num // 10 + num % 10
    return num

for num in range(10, 100):
    for den in range(num+1, 100):
        value = num / den
        cancel_num = cancel_9s(num)
        cancel_den = cancel_9s(den)
        cancel_value = cancel_num / cancel_den
        if value == cancel_value:
            print(num, "/", den, "==", cancel_num, "/", cancel_den)
