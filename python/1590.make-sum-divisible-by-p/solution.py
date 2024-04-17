# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    p: int = deserialize("int", read_line())
    ans = Solution().minSubarray(nums, p)
    print("\noutput:", serialize(ans, "integer"))
