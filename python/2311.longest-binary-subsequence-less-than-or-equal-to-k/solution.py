# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestSubsequence(s, k)
    print("\noutput:", serialize(ans, "integer"))
