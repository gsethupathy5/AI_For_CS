# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().uniqueLetterString(s)
    print("\noutput:", serialize(ans, "integer"))