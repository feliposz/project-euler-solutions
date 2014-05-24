{-
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
-}

euler1 = sum [x | x <- [1..999], x `mod` 3 == 0 || x `mod` 5 == 0]

--

aritProg f l q = (f + l) * q `div` 2

sumMult base maxVal = 
	let qty = maxVal `div` base
	    lastVal = base * qty
	 in aritProg base lastVal qty

euler1' = sumMult 3 999 + sumMult 5 999 - sumMult 15 999

--

sumDivisibleBy n = n*(p*(p+1)) `div` 2
	where p=999 `div` n

euler1'' = sumDivisibleBy(3)+sumDivisibleBy(5)-sumDivisibleBy(15)
