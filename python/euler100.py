from fractions import Fraction
from math import sqrt
from time import time

##half = 1/2
##
##blue = 3
##improve = 4/10
##while True:
##    red = blue * improve
##    while red > 0:
##        total = blue + red
##
##        probability = (blue/total) * ((blue - 1) / (total - 1))
##
##        dif = abs(probability - 0.5)
##
##        if dif < 0.00000000000001:
##            improve = red/blue
##            print("Blues: %d Reds: %d Total: %d Improve: %lf" % (blue, red, total, improve))
##            break
##        elif probability > half:
##            red += 1
##        elif probability < half:
##            break
##    blue += 1


##half = Fraction(1, 2)
##
##blue = 3
##improve = Fraction(4, 10)
##while True:
##    red = blue * improve
##    while red > 0:
##        total = blue + red
##
##        probability = Fraction(blue, total) * Fraction(blue - 1, total - 1)
##
##        if probability > half:
##            red += 1
##        elif probability < half:
##            break
##        else:
##            improve = Fraction(red, blue)
##            print("Blues: %d Reds: %d Total: %d" % (blue, red, total))
##            break
##    blue += 1

##half = 1/2
##
##blue = 15
##red = 6
##
##improve = 4/10
##while True:
##    while red > 0:
##        total = blue + red
##
##        probability = (blue/total) * ((blue - 1) / (total - 1))
##
##        dif = abs(probability - 0.5)
##
##        #print("Blues: %d Reds: %d Total: %d Probability: %lf Improve: %lf" % (blue, red, total, probability, improve))
##
##        if dif < 0.000000000000001:
##            improve = red/blue
##            print("Blues: %d Reds: %d Total: %d Improve: %lf" % (blue, red, total, improve))
##            break
##        elif probability > half:
##            red += 1
##        elif probability < half:
##            break
##    blue += 1
##    red = blue * improve


##start = time()
##
##half = Fraction(1, 2)
##
##total = 10 ** 6
##blue = int(total / sqrt(2)) + 1
##red = total - blue
##
##improve = Fraction(red, blue)
##found = False
##while not found:
##    while red > 0:
##        total = blue + red
##
##        probability = Fraction(blue, total) * Fraction(blue - 1, total - 1)
##
##        ##print("Blues: %d Reds: %d Probability: %s" % (blue, red, str(probability)))
##        
##        if probability > half:
##            red += 1
##        elif probability < half:
##            break
##        else:
##            improve = Fraction(red, blue)
##            print("Blues: %d Reds: %d Total: %d" % (blue, red, total))
##            found = True
##            break
##    blue += 1
##    red = int(blue * improve)
##
##print("Time:", time() - start)

"""
1/2 = (blue/total) * ((blue - 1) / (total - 1))

  blue * (blue-1)      1
------------------- = ---
total * (total - 1)    2

total = red + blue
total - red = blue

2 * (blue*blue - blue) = total*total - total


blue * (blue - 1) = (10**24 - 10**12) / 2

blue = sqrt((10**24 - 10**12) / 2)

"""

##Blues: 15 Reds: 6 Total: 21 Improve: 0.400000
##Blues: 85 Reds: 35 Total: 120 Improve: 0.411765
##Blues: 493 Reds: 204 Total: 697 Improve: 0.413793
##Blues: 2871 Reds: 1189 Total: 4060 Improve: 0.414141
##Blues: 16731 Reds: 6930 Total: 23661 Improve: 0.414201
##Blues: 97513 Reds: 40391 Total: 137904 Improve: 0.414211
##Blues: 568345 Reds: 235416 Total: 803761 Improve: 0.414213
##Blues: 3312555 Reds: 1372105 Total: 4684660 Improve: 0.414213
##Blues: 19306983 Reds: 7997214 Total: 27304197 Improve: 0.414214
##Blues: 112529326 Reds: 46611172 Total: 159140498 Improve: 0.414214

##Blues: 15 Reds: 6 Total: 21 Time: 0.000000
##Blues: 85 Reds: 35 Total: 120 Time: 0.010000
##Blues: 493 Reds: 204 Total: 697 Time: 0.017000
##Blues: 2871 Reds: 1189 Total: 4060 Time: 0.031000
##Blues: 16731 Reds: 6930 Total: 23661 Time: 0.090000
##Blues: 97513 Reds: 40391 Total: 137904 Time: 0.478000
##Blues: 568345 Reds: 235416 Total: 803761 Time: 2.464000
##Blues: 3312555 Reds: 1372105 Total: 4684660 Time: 13.987000
##Blues: 19306983 Reds: 7997214 Total: 27304197 Time: 80.909000
##Blues: 112529341 Reds: 46611179 Total: 159140520 Time: 469.191000
##From this line on, by: euler100.cpp
##Blues: 655869061 Reds: 271669860 Total: 927538921 Time: 36 
##Can't calculate anything beyond this, due to overflow...
##For example... (this is actually wrong - I only noticed when checking for overflow)
##Blues: 3822685023 Reds: 1583407981 Total: 5406093004 Time: 210

##start = time()
##
##LIMIT = 10**2 # Apparently this logic is correct, but it's still very slow
##blue = int(LIMIT / sqrt(2))
##red = LIMIT - blue
####blue -= 1
####red -= 1
##
##improve_num = red
##improve_den = blue
##total = 0
##found = False
##while not found:
##    while red > 0:
##        total = blue + red
##
##        num = blue * (blue - 1)
##        den = total * (total - 1)
##
####        print("Blues: %d Reds: %d Total: %d Time: %f" %
####              (blue, red, total, time() - start))
##        print(blue, red, num/den)
##
##        if num * 2 == den:
##            improve_num = red
##            improve_den = blue
##            print("Blues: %d Reds: %d Total: %d Time: %f" %
##                  (blue, red, total, time() - start))
##            found = True
##            break
##        elif num * 2 > den:
##            red += 1
##            #print("next red")
##        else:
##            #print("next blue")
##            break
##    blue += 1
##    red = blue * improve_num // improve_den

##Blues: 707119501233 Reds: 292898487629 Total: 1000017988862 Time: 1
##Blues: 707196729163 Reds: 292930476485 Total: 1000127205648 Time: 7
##Blues: 707212723591 Reds: 292937101594 Total: 1000149825185 Time: 8
##Blues: 707235343128 Reds: 292946470913 Total: 1000181814041 Time: 10
##Blues: 707251337556 Reds: 292953096022 Total: 1000204433578 Time: 15
##Blues: 707289951521 Reds: 292969090450 Total: 1000259041971 Time: 18
##Blues: 707305945949 Reds: 292975715559 Total: 1000281661508 Time: 19
##Blues: 707328565486 Reds: 292985084878 Total: 1000313650364 Time: 20
##Blues: 707344559914 Reds: 292991709987 Total: 1000336269901 Time: 22

start = time()
last_display = start

sqrt2 = 2**0.5 #sqrt(2)
blue = int(10**12 / sqrt2)

while True:
    total = int(blue * sqrt2)
    red = total - blue

    num = blue * (blue - 1)
    den = total * (total - 1)

    #print(total, blue, red, num/den)

    if time() - last_display > 60:
        print("[Progress] Blues: %d Reds: %d Total: %d Time: %d" %
              (blue, red, total, int(time() - start)))
        last_display = time()

    if num * 2 == den:
        print("Blues: %d Reds: %d Total: %d Time: %f" %
              (blue, red, total, time() - start))
        if total >= 10**12:
            break
    blue += 1


##Blues: 112529341 Reds: 46611179 Total: 159140520 Time: 6
##Blues: 655869061 Reds: 271669860 Total: 927538921 Time: 34
##Blues: 3822685023 Reds: 1583407981 Total: 5406093004 Time: 197
##Blues: 6989500985 Reds: 2895146102 Total: 9884647087 Time: 367
##Blues: 8301239106 Reds: 3438485822 Total: 11739724928 Time: 434
##b = 6989500985
##t = 9884647087
##print(Fraction(b, t) * Fraction(b-1, t-1))

