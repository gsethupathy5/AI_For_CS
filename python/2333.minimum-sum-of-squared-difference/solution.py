# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k1: int = deserialize("int", read_line())
    k2: int = deserialize("int", read_line())
    ans = Solution().minSumSquareDiff(nums1, nums2, k1, k2)
    print("\noutput:", serialize(ans, "long"))
