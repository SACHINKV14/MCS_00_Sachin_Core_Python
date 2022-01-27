"""
1360. Number of Days Between Two Dates
Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
"""
import datetime
class Solution:
    def daybetween(self, date1,date2: str) -> int:
        date1 = date1.split("-")
        date2 = date2.split("-")
        if date1[0]==date2[0]:
            x = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
            x1=int(x.strftime('%j'))
            # print(x1)
            y = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
            y1=int(y.strftime('%j'))
            # print(y1)
            max_d=max(x1,y1)
            min_d=min(x1,y1)
            res=max_d-min_d
            print(res)
        else:
            def numOfDays(date1, date2):
                return (date2 - date1).days

            # Driver program
            x1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
            y1 = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
            max_d = max(x1, y1)
            min_d = min(x1, y1)
            print((max_d-min_d).days)




# date1 = "2019-06-29"
# date2 = "2019-06-30"
date1 = "2020-01-15"
date2 = "2019-12-31"
s1=Solution()
s1.daybetween(date1,date2)