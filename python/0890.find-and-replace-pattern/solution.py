# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/find-and-replace-pattern/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    pattern: str = deserialize("str", read_line())
    ans = Solution().findAndReplacePattern(words, pattern)
    print("\noutput:", serialize(ans, "string[]"))
