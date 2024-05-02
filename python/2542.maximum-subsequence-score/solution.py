# Created by asetti2002 at 2024/05/01 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-subsequence-score/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(k + 1)]
        for i in range(k + 1):
            for j in range((k - i) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + nums1[i - 1] * nums2[j - 1]) if i > 0 else float('-inf')
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + nums1[i - 1] * nums2[j - 1]) if j > 0 else float('-inf')
        return dp[k][k]
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
