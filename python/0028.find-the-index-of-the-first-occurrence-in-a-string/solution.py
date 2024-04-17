# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    haystack: str = deserialize("str", read_line())
    needle: str = deserialize("str", read_line())
    ans = Solution().strStr(haystack, needle)
    print("\noutput:", serialize(ans, "integer"))
