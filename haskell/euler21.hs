{-
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
-}
import Data.List

-- 1)

divisors :: Integral a => a -> [a]
divisors n = nub $ concat [ [d, n `div` d] | d <- [1..sqn], n `mod` d == 0 ]
	where sqn = (floor (sqrt (fromIntegral n)))

sumDiv :: Integral a => a -> a
sumDiv n = (sum (divisors n)) - n

listSumDiv :: [(Integer, Integer)]
listSumDiv = [ (n, sumDiv n) | n <- [2..9999] ]

amicable :: [Integer]
amicable = [ a | (a, b) <- listSumDiv, a /= b, (b, a) `elem` listSumDiv ]

euler21 :: Integer
euler21 = sum amicable

-- 2)

amicable' :: [Integer]
amicable' = [ a+sumDiv(a) | a <- [2..9999], let b = sumDiv(a) in b > a && a == sumDiv(b) ]

euler21' :: Integer
euler21' = sum amicable'

-- 3)

-- TODO: Could make it faster by only trying prime divisors (pre-built list of primes)

