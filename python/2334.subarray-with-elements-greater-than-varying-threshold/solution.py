# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().validSubarraySize(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
