# Created by asetti2002 at 2024/04/25 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/distinct-subsequences-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26
        mod = 10**9 + 7
        for c in s:
            dp[ord(c) - ord('a')] = sum(dp) + 1
        return sum(dp) % mod
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().distinctSubseqII(s)
    print("\noutput:", serialize(ans, "integer"))
