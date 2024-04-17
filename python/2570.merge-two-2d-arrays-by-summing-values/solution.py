# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[List[int]] = deserialize("List[List[int]]", read_line())
    nums2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mergeArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[][]"))
