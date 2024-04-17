# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    multipliers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumScore(nums, multipliers)
    print("\noutput:", serialize(ans, "integer"))
