# Created by asetti2002 at 2024/05/01 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # write your code here
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestSquareStreak(nums)
    print("\noutput:", serialize(ans, "integer"))
