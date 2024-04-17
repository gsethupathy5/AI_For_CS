# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-subarray-min-product/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumMinProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
