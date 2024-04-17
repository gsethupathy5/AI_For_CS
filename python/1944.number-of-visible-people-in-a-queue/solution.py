# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canSeePersonsCount(heights)
    print("\noutput:", serialize(ans, "integer[]"))
