{-
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
-}
import Math.NumberTheory.Primes.Sieve (primeList, primeSieve)

-- 1) My first implementation using a reasonably fast "isPrime" function

isPrime :: Integer -> Bool
isPrime n
    | n == 1         = False
	| n < 4          = True
	| n `mod` 2 == 0 = False
	| n < 9          = True
	| n `mod` 3 == 0 = False
	| otherwise = 
		let sqn = (floor (sqrt (fromIntegral n))) + 1
	 	 in and [ n `mod` d /= 0 && n `mod` (d+2) /= 0 | d <- [5,11..sqn] ]

primes = [ p | p <- 2:[3,5..], isPrime p]

euler10 = sum (takeWhile (<2000000) primes)
-- Slow: 54 seconds

-- 2) A trial division, using the prime list itself for testing

primes' = 2:filter isPrime' [3,5..]
	where 
		isPrime' n =
			let sqn = (floor (sqrt (fromIntegral n))) + 1
		 	 in and [ n `mod` p > 0 | p <- takeWhile (<sqn) primes' ]

euler10' = sum (takeWhile (<2000000) primes')
-- A little faster: 37 seconds

{-
3) Using the arithmoi package from cabal that has a very efficient implementation of the Sieve of Erathostenes

Source & Info:
http://hackage.haskell.org/package/arithmoi
http://hackage.haskell.org/package/arithmoi-0.4.1.0/docs/Math-NumberTheory-Primes-Sieve.html
https://bitbucket.org/dafis/arithmoi/

Installation:
cabal install arithmoi

Import for using:
import Math.NumberTheory.Primes.Sieve (primeList, primeSieve)
-}

primesFast = primeList (primeSieve 2000000)

euler10fast = sum primesFast
-- Nearly instant (<1 second)

main = putStrLn (show euler10fast)
