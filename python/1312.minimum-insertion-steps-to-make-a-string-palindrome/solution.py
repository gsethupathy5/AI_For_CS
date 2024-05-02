# Created by asetti2002 at 2024/04/25 20:30
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for gap in range(1, n):
            left = 0
            for right in range(gap, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left+1][right-1]
                else:
                    dp[left][right] = min(dp[left+1][right], dp[left][right-1]) + 1
                left += 1
        
        return dp[0][n-1]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minInsertions(s)
    print("\noutput:", serialize(ans, "integer"))
