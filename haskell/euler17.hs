{-
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
-}

units = [ "zero"
        , "one"
        , "two"
        , "three"
        , "four"
        , "five"
        , "six"
        , "seven"
        , "eight"
        , "nine"
        , "ten"
        , "eleven"
        , "twelve"
        , "thirteen"
        , "fourteen"
        , "fifteen"
        , "sixteen"
        , "seventeen"
        , "eighteen"
        , "nineteen"
        ]

tens = [ "unit"
       , "ten"
       , "twenty"
       , "thirty"
       , "forty"
       , "fifty"
       , "sixty"
       , "seventy"
       , "eighty"
       , "ninety"
       ]

number2Text n
    | n == 0      = ""
	| n < 20      = units !! n
	| n < 100     = tens !! (n `div` 10) ++ number2Text (n `mod` 10)
	| n < 1000    = hundreds (n `div` 100) ++ hundredsTens (n `mod` 100)
    | n < 1000000 = number2Text (n `div` 1000) ++ "thousand" ++ number2Text (n `mod` 1000)
	where
		hundreds h = (units !! h) ++ "hundred"
		hundredsTens 0 = ""
		hundredsTens t = "and" ++ number2Text t

euler17 = length (concat (map number2Text [1..1000]))
