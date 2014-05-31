{-
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
-}

import Data.List

fibs = 1 : 1 : [ a + b | (a,b) <- zip fibs (tail fibs) ]

-- 1) My first attempt
euler25 = fst $ head $ dropWhile (\(n,x) -> length (show x) < 1000) $ zip [1..] fibs
-- (0.14 secs, 91924848 bytes)

-- 2) Based on a forum answer
euler25' = elemIndex 1000 $ map (length . show) fibs
-- (0.14 secs, 91890352 bytes)

-- 3) From http://projecteuler.net/thread=25
-- Using the property that fib n ~= phi * fib (n-1) and fib n ~= phi ^ n

phi = (1 + sqrt 5) / 2
log10 = logBase 10
euler25log = ( 999 + log10 (sqrt 5) ) / (log10 phi) + 1
