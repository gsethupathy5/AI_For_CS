# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-common-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    text1: str = deserialize("str", read_line())
    text2: str = deserialize("str", read_line())
    ans = Solution().longestCommonSubsequence(text1, text2)
    print("\noutput:", serialize(ans, "integer"))