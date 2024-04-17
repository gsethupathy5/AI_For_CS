# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-days-between-two-dates/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    date1: str = deserialize("str", read_line())
    date2: str = deserialize("str", read_line())
    ans = Solution().daysBetweenDates(date1, date2)
    print("\noutput:", serialize(ans, "integer"))
