# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/closest-subsequence-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    goal: int = deserialize("int", read_line())
    ans = Solution().minAbsDifference(nums, goal)
    print("\noutput:", serialize(ans, "integer"))
