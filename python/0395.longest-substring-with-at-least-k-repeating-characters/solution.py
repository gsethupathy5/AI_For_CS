# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestSubstring(s, k)
    print("\noutput:", serialize(ans, "integer"))
