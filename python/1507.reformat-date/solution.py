# Created by asetti2002 at 2024/04/25 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/reformat-date/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day, month, year = date.split()
        day = day[:-2].zfill(2)
        month = months[month]
        year = year
        return f"{year}-{month}-{day}"
# @lc code=end

if __name__ == "__main__":
    date: str = deserialize("str", read_line())
    ans = Solution().reformatDate(date)
    print("\noutput:", serialize(ans, "string"))
