{-
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
-}

--import Data.List
import qualified Data.Set as Set
import Math.NumberTheory.Primes.Factorisation

--divisors :: Integer -> [Integer]
--divisors n = [d | d <- [1..(n`div`2)], n `mod` d == 0 ]

sumDiv :: Integer -> Integer
--sumDiv n = sum (divisors n)
sumDiv n = divisorSum n - n

limit = 28123

-- Faster than built-in nub for this case!
nub' = Set.toList . Set.fromList

representables = 
	let abundants = [ n | n <- [1..limit], sumDiv n > n ]
	 in nub' [ a + b | a <- abundants, b <- abundants, a >= b, a + b <= limit ]

nonRepresentablesSum = sum [1..limit] - sum representables

main = putStrLn $ show $ nonRepresentablesSum
