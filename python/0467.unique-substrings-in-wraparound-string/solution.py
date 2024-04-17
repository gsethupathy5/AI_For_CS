# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findSubstringInWraproundString(s)
    print("\noutput:", serialize(ans, "integer"))
