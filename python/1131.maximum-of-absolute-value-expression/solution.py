# Created by asetti2002 at 2024/04/25 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-of-absolute-value-expression/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j))
        return ans
# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxAbsValExpr(arr1, arr2)
    print("\noutput:", serialize(ans, "integer"))
