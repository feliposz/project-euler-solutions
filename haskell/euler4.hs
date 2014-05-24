{-
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-}

isPalindrome :: Integer -> Bool
isPalindrome n = n == reversed n

reversed :: Integer -> Integer
reversed n = revHlp n 0
	where
		revHlp n r
			| n == 0 = r
			| otherwise = revHlp (n `div` 10) (r * 10 + n `mod` 10)

euler4 = maximum [p*q | p <- [100..999], q <- [p..999], isPalindrome (p*q)]

--

{- One easy improvement

If P is palindromic then:
P=100000x+10000y+1000z+100z+10y+x
P=100001x+10010y+1100z
P=11(9091x+910y+100z)
So one of the factors must be divisible by 11
-}

euler4' = maximum [p*q | p <- [11,22..999], q <- [p..999], isPalindrome (p*q)]
