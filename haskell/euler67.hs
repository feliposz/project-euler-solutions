{-
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
-}

combineDown :: (Num a, Ord a) => [a] -> [a] -> [a]
combineDown [] _ = []
combineDown (x:xs) (y:ys) = x + max y (head ys) : combineDown xs ys

-- Could be implemented as:
-- combineDown xs ys = zipWith (+) xs (zipWith max ys (tail ys))

str2triangle :: String -> [[Integer]]
str2triangle str = map splitNumbers (lines str)
	where splitNumbers s = map read (words s)

euler67 :: [[Integer]] -> Integer
euler67 triangle = head (foldr1 combineDown triangle)

main = do 
	str <- readFile  "../../Project Euler/triangle.txt"	
	putStrLn (show (euler67 (str2triangle str)))	
