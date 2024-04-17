# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/day-of-the-week/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    day: int = deserialize("int", read_line())
    month: int = deserialize("int", read_line())
    year: int = deserialize("int", read_line())
    ans = Solution().dayOfTheWeek(day, month, year)
    print("\noutput:", serialize(ans, "string"))
