# Created by asetti2002 at 2024/04/25 20:38
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-happy-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        return s[:lps[-1]] if lps[-1] > 0 else ""
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPrefix(s)
    print("\noutput:", serialize(ans, "string"))
