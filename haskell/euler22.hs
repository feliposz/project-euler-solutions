{-
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
-}

import Data.Char
import Data.List
import Data.List.Split

-- Calculate score for a single name/word
score :: String -> Integer
score name = sum $ map letterScore name
	where letterScore c = fromIntegral $ ord c - ord 'A' + 1

-- Split the input by comma and remove quotes
splitNames :: String -> [String]
splitNames str = splitOn "," $ filter (/= '"') str

-- Calculate the value by multiplying the name score by its position
euler22 :: String -> Integer
euler22 str = 
	let names = sort $ splitNames str
	 in sum [ n * score name | (n, name) <- zip [1..] names ]

main = do 
	str <- readFile  "../../Project Euler/names.txt"
	putStrLn $ show $ euler22 str
