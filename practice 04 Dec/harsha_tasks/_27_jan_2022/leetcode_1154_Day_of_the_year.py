"""
1154. Day of the Year
Given a string date representing a Gregorian calendar date formatted as YYYY - MM - DD,
return the day number of the year.
Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:
Input: date = "2019-02-10"
Output: 41
"""
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        date1 = date.split("-")
        # print(date1)
        x = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
        print(x.strftime('%j'))


date = "2019-01-09"
# date = "2019-02-10"

s1=Solution()
s1.dayOfYear(date)


