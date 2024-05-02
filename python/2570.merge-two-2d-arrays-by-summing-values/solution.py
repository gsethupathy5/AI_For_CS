# Created by asetti2002 at 2024/05/01 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        ids = set([x[0] for x in nums1] + [x[0] for x in nums2])
        
        for i in ids:
            val1 = next((x[1] for x in nums1 if x[0] == i), 0)
            val2 = next((x[1] for x in nums2 if x[0] == i), 0)
            res.append([i, val1 + val2])

        return res
# @lc code=end

if __name__ == "__main__":
    nums1: List[List[int]] = deserialize("List[List[int]]", read_line())
    nums2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mergeArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[][]"))
