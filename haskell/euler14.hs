-- to measure execution time of functions: :set +s 
import Data.List (unfoldr)

-- 1) First attempt

collatz :: Integer -> [Integer]
collatz n
	| n == 1    = n:[]
	| even n    = n:collatz (n `div` 2)
	| otherwise = n:collatz (3 * n + 1)

sequences = [ (length (collatz n), n) | n <- [1,3..999999] ]

euler14 = maximum sequences
--(525,837799)
--(163.94 secs, 29678855136 bytes) Trying all numbers
--(85.80 secs,  15549985064 bytes) Trying only even starting numbers

-- 2) Instead of using the list approach, trying to count the length only

collatzLength :: Integer -> Integer
collatzLength n
	| n == 1    = 1
	| even n    = 1 + collatzLength (n `div` 2)
	| otherwise = 1 + collatzLength (3 * n + 1)

euler14' = maximum [ (collatzLength n, n) | n <- [1,3..999999] ]
--(525,837799)
--(265.28 secs, 47562177380 bytes) O.o Really?!?

-- 3) Same as above with possible tail recursion optimization ?

collatzLength' :: Integer -> Integer -> Integer
collatzLength' n len
	| n == 1    = len + 1
	| even n    = collatzLength' (n `div` 2) (len + 1)
	| otherwise = collatzLength' (3 * n + 1) (len + 1)

euler14tail = maximum [ (collatzLength' n 0, n) | n <- [1,3..999999] ]
-- (156.28 secs, 31628196972 bytes) first attempt, no strict
-- (186.80 secs, 32339904244 bytes) attempting to use $! - surprise, even worse!


-- 4) Using the unfoldr function

collatzUnfoldr start = unfoldr nextCollatz start
	where nextCollatz n
			| n <= 0 = Nothing
			| n == 1 = Just (1, 0)
			| even n = Just (n, n `div` 2)
			| odd  n = Just (n, 3 * n + 1)

euler14unfoldr = maximum [ (length (collatzUnfoldr n), n) | n <- [1,3..999999] ]
-- (81.42 secs, 12955653416 bytes)

main = print (show euler14unfoldr)
-- The first 3 versions run in under 3 seconds compiled with -O2 switch and only counting odd sequences
-- The fourth run in 4 seconds compiled even thought it was the fastest version interpreted

