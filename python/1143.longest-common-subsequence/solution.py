# Created by asetti2002 at 2024/04/25 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-common-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
# @lc code=end

if __name__ == "__main__":
    text1: str = deserialize("str", read_line())
    text2: str = deserialize("str", read_line())
    ans = Solution().longestCommonSubsequence(text1, text2)
    print("\noutput:", serialize(ans, "integer"))
