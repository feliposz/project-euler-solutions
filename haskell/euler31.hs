{-
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
-}

coins' 0 _ = 1
coins' value previous = sum [ coins' (value-coin) coin 
                            | coin <- [1,2,5,10,20,50,100,200]
                            , coin <= value
                            , coin <= previous
                            ]

coins value = coins' value 200

euler31 = coins 200
-- 
-- (17.38 secs, 2791918820 bytes)

--2) http://projecteuler.net/overview=031 (A)

coinValues = [ 1, 2, 5, 10, 20, 50, 100 , 200, -1 ]
ways' target avc res
	| avc <= 0    = 1
    | target > 0  = ways' (target - coinValues !! avc) avc (res + ways' target (avc-1) 0)
    | otherwise   = res
ways amount = ways' amount 7 0

euler31' = ways 200
-- (0.17 secs, 25812320 bytes)

--3) http://projecteuler.net/overview=031 (B)

euler31fast = looper 0 (coinValues !! 1) (0:1:(replicate 200 0))

coinValues' = [ 0, 1, 2, 5, 10, 20, 50, 100 , 200, -1 ]
looper i j ways
	| i > 8     = ways !! 200
	| j > 200   = looper (i+1) (coinValues!!(i+1)) ways
	| otherwise = looper i (j+1) newWays
	where newWays = take j ways ++ [ways!!j + ways!!(j-coinValues!!i)] ++ drop (j+1) ways

-- Not working properly. Some off-by-1 errors in the way