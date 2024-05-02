# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-days-between-two-dates/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        
        date_format = "%Y-%m-%d"
        d1 = datetime.datetime.strptime(date1, date_format)
        d2 = datetime.datetime.strptime(date2, date_format)
        
        return abs((d2 - d1).days)
# @lc code=end

if __name__ == "__main__":
    date1: str = deserialize("str", read_line())
    date2: str = deserialize("str", read_line())
    ans = Solution().daysBetweenDates(date1, date2)
    print("\noutput:", serialize(ans, "integer"))
