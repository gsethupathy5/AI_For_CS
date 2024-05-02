# Created by asetti2002 at 2024/05/01 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        cost = 0
        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                cost += min(nums1.count(nums1[i]), nums2.count(nums1[i])) - 1
        if cost % 2 != 0:
            cost += 1
        return cost if cost != 0 else -1
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTotalCost(nums1, nums2)
    print("\noutput:", serialize(ans, "long"))
