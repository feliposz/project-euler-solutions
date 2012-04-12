def euler8():
    """Solves problem 7 of Project Euler."""
    big  = "73167176531330624919225119674426574742355349194934"
    big += "96983520312774506326239578318016984801869478851843"
    big += "85861560789112949495459501737958331952853208805511"
    big += "12540698747158523863050715693290963295227443043557"
    big += "66896648950445244523161731856403098711121722383113"
    big += "62229893423380308135336276614282806444486645238749"
    big += "30358907296290491560440772390713810515859307960866"
    big += "70172427121883998797908792274921901699720888093776"
    big += "65727333001053367881220235421809751254540594752243"
    big += "52584907711670556013604839586446706324415722155397"
    big += "53697817977846174064955149290862569321978468622482"
    big += "83972241375657056057490261407972968652414535100474"
    big += "82166370484403199890008895243450658541227588666881"
    big += "16427171479924442928230863465674813919123162824586"
    big += "17866458359124566529476545682848912883142607690042"
    big += "24219022671055626321111109370544217506941658960408"
    big += "07198403850962455444362981230987879927244284909188"
    big += "84580156166097919133875499200524063689912560717606"
    big += "05886116467109405077541002256983155200055935729725"
    big += "71636269561882670428252483600823257530420752963450"

    maxprod = 1
    for i in range(len(big) - 5):
        prod = 1
        for j in map(int, big[i:i+5]):
            prod *= j
        maxprod = max(prod, maxprod)
    print(maxprod)

if __name__ == "__main__":
    euler8()