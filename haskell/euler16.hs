import Data.Char

-- 1) Using built-in functions

largeNum = 2^1000

digits n = map digitToInt (show n)

euler16 = sum $ digits largeNum

-- 2) A recursive version

sumDigits 0 = 0
sumDigits n = n `mod` 10 + sumDigits (n `div` 10)

euler16' = sumDigits largeNum
