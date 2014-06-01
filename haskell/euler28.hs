{-
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
-}

--urDiag n = map (\x -> x^2) [1,3,5..n]
--drDiag n = map (\x -> x^2 - x + 1) [1,3,5..n]
--ulDiag n = map (\x -> x^2 - x*2 + 2) [1,3,5..n]
--dlDiag n = map (\x -> x^2 - x*3 + 3) [1,3,5..n]


sumDiag n = 1 + sum [ 4*x^2 - 6*x + 6 | x <- [3,5..n] ]

euler28 = sumDiag 1001
--669171001
--(0.00 secs, 1587040 bytes)
