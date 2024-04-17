# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-highest-altitude/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    gain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestAltitude(gain)
    print("\noutput:", serialize(ans, "integer"))
