{-
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
-}

import Data.MemoTrie (memo2)
import Data.List
import Data.Array

-- Not memoized (too slow above 10x10)
latticePaths i 0 = 1
latticePaths 0 j = 1
latticePaths i j = (latticePaths (i-1) j) + (latticePaths i (j-1))

-- Memoized (not working... about same time as above)
lattice :: Integer -> Integer -> Integer
lattice i 0 = 1
lattice 0 j = 1
lattice i j = latticeMemo (i-1) j + latticeMemo i (j-1)
	where latticeMemo = memo2 lattice

euler15 = lattice 10 10

--main = print (show euler15)



-- Got this from the forum (http://projecteuler.net/thread=15;page=2)
-- Instantaneous

tabulate :: Ix t => (t, t) -> (t -> e) -> Array t e
tabulate bounds f = array bounds [(i,f i) | i <- range bounds]

dp :: Ix i => (i, i) -> ((i -> e) -> i -> e) -> i -> e
dp bounds f = (memo!) where memo = tabulate bounds (f (memo!))

p15 :: (Num t, Num e, Ix t) => t -> e
p15 n = dp ((0,0),(n,n)) f (n,n) where
 f rec (x,y) | x == 0 || y == 0 = 1
             | otherwise = rec (x-1,y) + rec (x,y-1)

--main = print $ p15 20


-- Using combinatorics
-- 40!/(20!*20!)
euler15comb = let fac n = product [1..n] in fac 40 `div` (fac 20 ^ 2)
