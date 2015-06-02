{-
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

-- Inefficient, generating all possible triplets!

isPythagorean a b c = a*a + b*b == c*c

triplets = [ (a,b,c) | c <- [1..]
                     , b <- [1..(c-1)]
                     , a <- [1..(b-1)]
                     , isPythagorean a b c ]

euler9 = head [ a*b*c | (a,b,c) <- triplets, a+b+c == 1000 ]

-- http://projecteuler.net/overview=009

-- Reducing one variable, generating only triplets with perimeter = 1000

triplets' s = [ (a,b,s-a-b) | a <- [3..(s-3) `div` 3]
                            , b <- [a..(s-1-a) `div` 2]
                            , isPythagorean a b (s-a-b) ]

euler9' = let (a,b,c) = head (triplets' 1000) in a*b*c
