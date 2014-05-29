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

-- Using library functions (my implementation is on euler19.hs)

import Data.Time.Calendar
import Data.Time.Calendar.OrdinalDate

initial = fromGregorian 1901 1 1
final = fromGregorian 2000 12 31
period = [initial..final]

isSundayFirst :: Day -> Bool
isSundayFirst date = 
	let (year, month, day) = toGregorian date
	    (week, weekday) = mondayStartWeek date
	 in day == 1 && weekday == 7

sundayFirsts = filter isSundayFirst period

euler19 = length sundayFirsts

-- A more direct approach

euler19' = sum [ 1 | m <- [1..12], y <- [1901..2000], snd (mondayStartWeek (fromGregorian y m 1)) == 7 ]

