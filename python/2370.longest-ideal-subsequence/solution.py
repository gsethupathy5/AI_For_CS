# Created by asetti2002 at 2024/05/01 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-ideal-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        def find_longest_ideal_string(s, k):
            n = len(s)
            dp = [1] * n
            for i in range(1, n):
                for j in range(i):
                    if abs(ord(s[i]) - ord(s[j])) <= k:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        return find_longest_ideal_string(s, k)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestIdealString(s, k)
    print("\noutput:", serialize(ans, "integer"))
