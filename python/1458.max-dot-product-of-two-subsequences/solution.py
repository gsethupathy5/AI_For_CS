# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDotProduct(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
