"""
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
"""
import datetime
import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        x = datetime.datetime(year,month,day)
        print(calendar.day_name[x.weekday()] )


# day = 31
# month = 8
# year = 2019

# day = 18
# month = 7
# year = 1999

# day = 15
# month = 8
# year = 1993

day = 14
month = 2
year = 1994

s1=Solution()
s1.dayOfTheWeek(day,month,year)