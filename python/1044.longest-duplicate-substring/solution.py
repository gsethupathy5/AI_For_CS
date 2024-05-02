# Created by asetti2002 at 2024/04/25 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-duplicate-substring/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Add your solution here
        return ""
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestDupSubstring(s)
    print("\noutput:", serialize(ans, "string"))
