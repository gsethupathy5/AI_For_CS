# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().smallestSubsequence(s)
    print("\noutput:", serialize(ans, "string"))