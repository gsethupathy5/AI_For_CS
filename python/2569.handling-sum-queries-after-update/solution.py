# Created by asetti2002 at 2024/05/01 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/handling-sum-queries-after-update/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        def flip(nums1, l, r):
            for i in range(l, r + 1):
                nums1[i] = 1 - nums1[i]
        
        res = []
        for query in queries:
            if query[0] == 1:
                flip(nums1, query[1], query[2])
            elif query[0] == 2:
                p = query[1]
                for i in range(len(nums2)):
                    nums2[i] += nums1[i] * p
            elif query[0] == 3:
                res.append(sum(nums2))
        
        return res
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().handleQuery(nums1, nums2, queries)
    print("\noutput:", serialize(ans, "long[]"))
