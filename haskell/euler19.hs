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
data Month = January | February | March | April | May | June | July | August | September | October | November | December deriving (Enum, Eq, Ord, Show)
data Date = Date Year Month Day deriving (Eq, Ord, Show)
data WeekDay = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday deriving (Enum, Eq, Show)

-- Quick check if a year is a leap year
isLeapYear :: Year -> Bool
isLeapYear y = y `mod` 400 == 0 || (y `mod` 4 == 0 && y `mod` 100 /= 0)

-- Determine the next day of a given date
next :: Date -> Date
next (Date y m d)
	| m == December && d == 31 = Date (y+1) January 1
	| d == 31                  = Date y (succ m) 1
	| m == February && d == 28 = if isLeapYear y then Date y February 29 else Date y March 1
	| m == February && d == 29 = Date y March 1
	| m `elem` [April, June, September, November] && d == 30 = Date y (succ m) 1
	| otherwise = Date y m (d+1)

-- The first known Monday given in the problem description
initialMonday :: Date
initialMonday = Date 1900 January 1

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
period = dropWhile (\(w,d) -> d < (Date 1901 January 1)) (takeWhile (\(w,d) -> d <= (Date 2000 December 31)) days)

-- Filter only the sundays that happened in the first of the month
sundayFirsts :: [(WeekDay, Date)]
sundayFirsts = filter (\(w,Date y m d) -> w == Sunday && d == 1) period

-- Count them
euler19 :: Int
euler19 = length sundayFirsts
