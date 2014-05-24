{-
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
-}

-- Brute force

divisors = [2..20]

divAll n = and (map (\d -> n `mod` d == 0) divisors)

euler5 = head $ filter divAll [20,40..]

{- No programming, just finding the Least Common Multiple
1 2 3 4 5 6 7 8 9 10 | 2
1 1 3 2 5 3 7 4 9 5  | 2
1 1 3 1 5 3 7 2 9 5  | 2
1 1 3 1 5 3 7 1 9 5  | 3
1 1 1 1 5 1 7 1 3 5  | 3
1 1 1 1 5 1 7 1 1 5  | 5
1 1 1 1 1 1 7 1 1 1  | 7
1 1 1 1 1 1 1 1 1 1  | 1
                     = 2*2*2*3*3*5*7

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | 2
1 1 3 2 5 3 7 4 9  5 11  6 13  7 15  8 17  9 19 10 | 2
1 1 3 1 5 3 7 2 9  5 11  3 13  7 15  4 17  9 19  5 | 2
1 1 3 1 5 3 7 1 9  5 11  3 13  7 15  2 17  9 19  5 | 2
1 1 3 1 5 3 7 1 9  5 11  3 13  7 15  1 17  9 19  5 | 3
1 1 1 1 5 1 7 1 3  5 11  1 13  7  5  1 17  3 19  5 | 3
1 1 1 1 5 1 7 1 1  5 11  1 13  7  5  1 17  1 19  5 | 5
1 1 1 1 1 1 7 1 1  1 11  1 13  7  1  1 17  1 19  1 | 7
1 1 1 1 1 1 1 1 1  1 11  1 13  1  1  1 17  1 19  1 | 11 * 13 * 17 * 19
                                                   = 2*2*2*2*3*3*5*7*11*13*17*19
-}

-- Or, by applying the lcm function on all divisors
euler5' = foldl1 lcm divisors
