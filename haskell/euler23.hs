{-
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
-}

import Data.List
import Math.NumberTheory.Primes.Factorisation

--divisors :: Integral a => a -> [a]
--divisors n = nub $ concat [ [d, n `div` d] | d <- [1..sqn], n `mod` d == 0 ]
--	where sqn = (floor (sqrt (fromIntegral n)))

sumDiv :: Integer -> Integer
sumDiv n = divisorSum n - n

isAbundant :: Integer -> Bool
isAbundant n = sumDiv n > n

abundants :: [Integer]
abundants = [ n | n <- [1..], isAbundant n ]

infiniteElem :: (Ord a) => a -> [a] -> Bool
infiniteElem x list = case dropWhile (< x) list of
  [] -> False
  (v:_) -> v == x

isAbundantSum n =
	let tests = takeWhile (<= (n `div` 2)) abundants
	 in if tests == []
	 	  then False
	 	  else or [(n - a) `infiniteElem` abundants | a <- tests ]

isNonAbundantSum = not . isAbundantSum

nonAbundantSums = [ n | n <- [1..28123], isNonAbundantSum n ]
-- (1970.70 secs, 1005367104 bytes)
-- 4179871

euler23 = sum nonAbundantSums

main = putStrLn $ show $ euler23
