{-
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
-}

-- Some custom data types to help define the problem
type Year = Int
type Day = Int
type Month = Int
data Date = Date Year Month Day deriving (Eq, Ord, Show)
data WeekDay = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday deriving (Enum, Eq, Show)

-- Quick check if a year is a leap year
isLeapYear :: Year -> Bool
isLeapYear y = y `mod` 400 == 0 || (y `mod` 4 == 0 && y `mod` 100 /= 0)

-- Determine the next day of a given date
next :: Date -> Date
next (Date y m d)
	| m == 12 && d == 31 = Date (y+1) 1 1
	| d == 31            = Date y (m+1) 1
	| m == 2 && d == 28  = if isLeapYear y then Date y m 29 else Date y 3 1
	| m == 2 && d == 29  = Date y 3 1
	| m `elem` [4, 6, 9, 11] && d == 30 = Date y (succ m) 1
	| otherwise = Date y m (d+1)

-- The first known Monday given in the problem description
initialMonday :: Date
initialMonday = Date 1900 1 1

-- An infinite sequence of dates starting from initialMonday
calendar :: [Date]
calendar = iterate next initialMonday

-- An infinite cycle of the days of the week
weekdays :: [WeekDay]
weekdays = cycle [Monday .. Sunday]

-- Pairing the day of the week with an actual date beginning on a known Monday (see above)
days :: [(WeekDay, Date)]
days = zip weekdays calendar

-- Filter the given period
period :: [(WeekDay, Date)]
period = dropWhile (\(w,d) -> d < (Date 1901 1 1)) (takeWhile (\(w,d) -> d <= (Date 2000 12 31)) days)

-- Filter only the sundays that happened in the first of the month
sundayFirsts :: [(WeekDay, Date)]
sundayFirsts = filter (\(w,Date y m d) -> w == Sunday && d == 1) period

-- Count them
euler19 :: Int
euler19 = length sundayFirsts

{-
instance Enum Date where
	toEnum date = 
		let y = (date `div` 10000) 
		    m = (date `div` 100 `mod` 100) 
		    d = (date `mod` 100)
		    test1 = m `elem` [4, 6, 9, 11] && d > 30
		    test2 = m == 2 && d > 28 && not (isLeapYear y)
		    test3 = m >= 1 && m <= 12
		 in if test1 && test2 && test3
		 	  then Date y m d
		 	  else InvalidDate date

	fromEnum (Date y m d) = y*10000 + m*100 + d

	succ date = next date		
-}
