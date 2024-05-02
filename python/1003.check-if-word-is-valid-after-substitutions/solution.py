# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isValid(self, s: str) -> bool:
        while "abc" in s:
            s = s.replace("abc", "")
        return s == ""
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
