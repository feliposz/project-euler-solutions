{-
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
-}

units :: Integer -> String
units  0 = ""
units  1 = "one"
units  2 = "two"
units  3 = "three"
units  4 = "four"
units  5 = "five"
units  6 = "six"
units  7 = "seven"
units  8 = "eight"
units  9 = "nine"
units 10 = "ten"
units 11 = "eleven"
units 12 = "twelve"
units 13 = "thirteen"
units 14 = "fourteen"
units 15 = "fifteen"
units 16 = "sixteen"
units 17 = "seventeen"
units 18 = "eighteen"
units 19 = "nineteen"

tens :: Integer -> String
tens 2 = "twenty"
tens 3 = "thirty"
tens 4 = "forty"
tens 5 = "fifty"
tens 6 = "sixty"
tens 7 = "seventy"
tens 8 = "eighty"
tens 9 = "ninety"

hundreds :: Integer -> Integer -> String
hundreds h 0 = units h ++ "hundred"
hundreds h t = units h ++ "hundredand" ++ number2Text t

number2Text n
    | n == 0      = ""
	| n < 20      = units n
	| n < 100     = tens (n `div` 10) ++ number2Text (n `mod` 10)
	| n < 1000    = hundreds (n `div` 100) (n `mod` 100)
    | n < 1000000 = number2Text (n `div` 1000) ++ "thousand" ++ number2Text (n `mod` 1000)

euler17 = length (concat (map number2Text [1..1000]))
