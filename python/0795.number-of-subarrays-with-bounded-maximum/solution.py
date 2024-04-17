# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().numSubarrayBoundedMax(nums, left, right)
    print("\noutput:", serialize(ans, "integer"))
