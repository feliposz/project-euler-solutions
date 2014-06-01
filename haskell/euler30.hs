{-
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
-}
import Data.Char
import Data.List

limit = 6 * 9^5 -- http://projecteuler.net/thread=30

sum5 x = sum $ map (\d -> digitToInt d ^ 5) $ show x

d5p = filter (\x -> sum5 x == x) [2..limit]

euler30 = sum d5p
-- 443839
-- (2.73 secs, 1270207552 bytes)
