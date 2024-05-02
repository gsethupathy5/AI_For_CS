# Created by asetti2002 at 2024/04/25 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/uncrossed-lines/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (nums1[i - 1] == nums2[j - 1]))
        return dp[m][n]
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxUncrossedLines(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
