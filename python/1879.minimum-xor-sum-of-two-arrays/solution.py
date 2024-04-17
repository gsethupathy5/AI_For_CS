# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumXORSum(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
