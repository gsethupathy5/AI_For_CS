# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-complete-trips/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    totalTrips: int = deserialize("int", read_line())
    ans = Solution().minimumTime(time, totalTrips)
    print("\noutput:", serialize(ans, "long"))
