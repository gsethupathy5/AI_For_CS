# Created by asetti2002 at 2024/04/25 20:24
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = set1.difference(set2)
        diff2 = set2.difference(set1)
        return [list(diff1), list(diff2)]
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDifference(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[][]"))
