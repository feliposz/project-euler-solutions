{-
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
-}

-- Slow, using a "naive" sieve of eratosthenes

primes :: [Integer]
primes = sieve [2..]
	where
		sieve (p:ns) = p : sieve [n | n <- ns, n `mod` p /= 0]

euler7 = primes !! 10000

-- Faster, doing a fast test for primality

isPrime :: Integer -> Bool
isPrime n
	| n < 2     = False
	| n == 2    = True
	| otherwise = 
		let sqn = (floor (sqrt (fromIntegral n))) + 1
	 	 in and [ n `mod` d /= 0 | d <- [2..sqn] ]

primes' = [ p | p <- [2..], isPrime p]

euler7' = primes' !! 10000

-- http://projecteuler.net/overview=007

isPrime' :: Integer -> Bool
isPrime' n
    | n == 1         = False
	| n < 4          = True
	| n `mod` 2 == 0 = False
	| n < 9          = True
	| n `mod` 3 == 0 = False
	| otherwise = 
		let sqn = (floor (sqrt (fromIntegral n))) + 1
	 	 in and [ n `mod` d /= 0 && n `mod` (d+2) /= 0 | d <- [5,11..sqn] ]

primes'' = [ p | p <- [2..], isPrime' p]

--euler7'' = primes'' !! 10000
