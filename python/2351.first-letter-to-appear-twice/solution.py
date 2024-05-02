# Created by asetti2002 at 2024/05/01 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/first-letter-to-appear-twice/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                return s[i]
            seen.add(s[i])
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().repeatedCharacter(s)
    print("\noutput:", serialize(ans, "character"))
