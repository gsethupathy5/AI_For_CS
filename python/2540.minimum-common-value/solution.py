# Created by asetti2002 at 2024/05/01 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-common-value/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2)) if set(nums1) & (set(nums2)) else -1
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getCommon(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
