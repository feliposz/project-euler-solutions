import Data.List (foldl1')
import Math.NumberTheory.Primes.Testing (isPrime)
--import Control.Parallel.Strategies (using, parList, rseq)

-- isPrime :: Integer -> Bool
-- isPrime n
-- 	| n < 2     = False
-- 	| n == 2    = True
-- 	| otherwise = 
-- 		let sqn = (floor (sqrt (fromIntegral n))) + 1
-- 	 	 in and [ n `mod` d /= 0 | d <- [2..sqn] ]

formula :: Integer -> Integer -> Integer -> Integer
formula a b n = n*n + a*n + b

test :: Integer -> Integer -> Integer -> Bool
test a b n = isPrime $ formula a b n

primeSequence :: Integer -> Integer -> [Integer]
primeSequence a b = takeWhile (test a b) [0..]

sequenceLength :: Integer -> Integer -> Int
sequenceLength a b = length $ primeSequence a b

maximum' = foldl1' max

sequenceLenghts = [ (sequenceLength a b, a, b) 
                  | a <- [(-999)..999]
                  , b <- [(-999)..999] 
                  ] -- `using` parList rseq

euler27 = maximum' sequenceLenghts

main = print $ a * b
	where (len, a, b) = euler27
--(71,-61,971)
--(30.64 secs, 5773882468 bytes) -- using my isPrime implementation
--(15.15 secs, 2572417912 bytes) -- using Math.NumberTheory.Primes.Testing.isPrime
