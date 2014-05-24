{-
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
-}

{- too slow!!!
factors :: Integer -> [Integer]
factors n = [f | f <- [1..n], n `mod` f == 0]

primes :: [Integer]
primes = sieve [2..]
	where
		sieve (p:ns) = p : sieve [n | n <- ns, n `mod` p /= 0]

primeFactors :: Integer -> [Integer]
primeFactors n = 
	let sqn = floor (sqrt (fromIntegral n))
	 in [ p | p <- takeWhile (<sqn) primes, n `mod` p == 0 ]

euler3'' = last $ primeFactors 13195 --600851475143
-}

maxPrimeFactor :: Integer -> Integer
maxPrimeFactor n = tryFactor n 2
	where
		tryFactor n f
			| n < f          = f
			| n `mod` f == 0 = tryFactor (n `div` f) f
			| f == 2         = tryFactor n (f + 1) -- 1st improvement: 2 is special
			| otherwise      = tryFactor n (f + 2) -- all other factors are odd

euler3 = maxPrimeFactor 600851475143 --13195 

-- http://projecteuler.net/overview=003

isqrt :: Integer -> Integer
isqrt n = floor (sqrt (fromIntegral n))

tryFactor :: Integer -> Integer -> Integer -> Integer -> Integer
tryFactor n 2 lastF maxF
	| n `mod` 2 == 0 = tryFactor (n `div` 2) 2 2 maxF 
	| otherwise      = tryFactor n 3 2 (isqrt n)
tryFactor n f lastF maxF
	| n == 1         = lastF
	| f > maxF       = n
	| n `mod` f == 0 = let newN = (n `div` f) in tryFactor newN f f (isqrt newN)
	| otherwise      = tryFactor n (f+1) f (isqrt n)

maxPrimeFactor' :: Integer -> Integer
maxPrimeFactor' n = tryFactor n 2 1 (isqrt n)

euler3' = maxPrimeFactor 600851475143
