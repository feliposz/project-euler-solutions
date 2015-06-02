{-
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
-}

import Data.List

elements = "0123456789"

-- 1) First implementation using library

perms = permutations elements

sorted = sort perms

euler24 = sorted !! 999999
-- (5.35 secs, 1576058508 bytes)

-- 2) After trying to implement my own permutations' I found this one: http://stackoverflow.com/questions/11358979/list-permutations-in-haskell

-- Less efficient but produces lexicographic ordered permutations (if elements are ordered of course)
permutations' :: Eq a => [a] -> [[a]]
permutations' [] = [[]]
--These two versions are equivalent in performance, but I think the second is easier to understand
--permutations' xs = concatMap (\x -> map (x:) $ permutations' $ delete x xs) xs -- (4.27 secs, 1294792708 bytes)
permutations' xs = [ x:ys | x <- xs, ys <- permutations' (delete x xs) ] -- (4.27 secs, 1049940744 bytes)

perms' = permutations' elements

euler24' = perms' !! 999999


-- 3) Using clever comprehension

permsR = [ [a,b,c,d,e,f,g,h,i,j] | a <- elements
                                 , b <- elements \\ [a]
                                 , c <- elements \\ [a,b]
                                 , d <- elements \\ [a,b,c]
                                 , e <- elements \\ [a,b,c,d]
                                 , f <- elements \\ [a,b,c,d,e]
                                 , g <- elements \\ [a,b,c,d,e,f]
                                 , h <- elements \\ [a,b,c,d,e,f,g]
                                 , i <- elements \\ [a,b,c,d,e,f,g,h]
                                 , j <- elements \\ [a,b,c,d,e,f,g,h,i]
                                 ]

euler24R = permsR !! 999999
-- (3.15 secs, 1687931116 bytes)

-- 4) Repeated digits

hasRepeated [] = False
hasRepeated (x:xs) = x `elem` xs || hasRepeated xs

-- Actually, I needed to guarantee that all digits are present, but I abandoned this
-- because I liked method 3 better. I kept this hasRepeated though..

--permsX = [ x | x <- [0123456789..9876543210], not (hasRepeated (show x))]

--euler24X = permsX !! 999999
