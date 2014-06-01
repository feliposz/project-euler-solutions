import Data.List

-- d = divisor to be tested
-- r = current remainder of the division
-- rs = remainders already encountered in the division process. If a remainder repeats then a recurring cycle was found
-- i = counter of the number of iterations needed (aka. number of digits after the dot)
-- str = string representation of the number 1/d

-- returns the size of the recurring cycle
recCycle :: (Integral a, Num t, Show a) => a -> t
recCycle d = size
	where (size, str, rs) = recHelp d 0 [] 10 ""

-- prints the number (for debugging)
recPrint :: (Integral a, Show a) => a -> String
recPrint d = str
	where (size, str, rs) = recHelp d 0 [] 10 ""

-- recursive helper function used above
recHelp :: (Integral a, Num t, Show a) => a -> t -> [a] -> a -> String -> (t, String, [a])
recHelp d i rs r str
   	| r == 0      = (0, str, rs) -- No remainder means an exact division
	| r `elem` rs = (i, str ++ "...", rs) -- Remainder repeated, cycle found. Return the number of digits of the cycle
	| r < d       = recHelp d (i + 1) (r:rs) (r * 10)            (str ++ "0") -- remainder can't be divided, add a digit to it and 0 to the quotient string
	| otherwise   = recHelp d (i + 1) (r:rs) ((r `mod` d) * 10)  (str ++ show (r `div` d)) -- find the next remainder, add it to the remainder "memory" and add the next digit of the division to the quotient string

euler26 :: Integer
euler26 = maximum [recCycle d | d <- [1..999] ]


-- (actually... this isn't necessary for this case!!!)
	-- | r `elem` rs = (i - r `indexRev` rs, str ++ "...", rs) -- Remainder repeated, cycle found. Subtract from the number of digits to find the size of the cycle
	-- where 
	--  	x `indexRev` xs = head $ x `elemIndices` (reverse xs) -- A helper function to find the position of the repeated remainder
