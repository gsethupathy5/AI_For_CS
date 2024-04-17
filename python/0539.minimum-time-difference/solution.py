# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-difference/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    timePoints: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findMinDifference(timePoints)
    print("\noutput:", serialize(ans, "integer"))
