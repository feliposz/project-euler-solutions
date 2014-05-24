{-
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-}

sumOfSquares n = sum $ map (^2) [1..n]
squareOfSum n = (sum [1..n]) ^ 2

euler6 = squareOfSum 100 - sumOfSquares 100

-- http://projecteuler.net/overview=006

sumOfSquares' n = (2 * n + 1) * (n + 1) * n `div` 6
squareOfSum' n = (n * (n+1) `div` 2) ^ 2

euler6' = squareOfSum' 100 - sumOfSquares' 100
