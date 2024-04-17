# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/teemo-attacking/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    timeSeries: List[int] = deserialize("List[int]", read_line())
    duration: int = deserialize("int", read_line())
    ans = Solution().findPoisonedDuration(timeSeries, duration)
    print("\noutput:", serialize(ans, "integer"))
