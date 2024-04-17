# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/keyboard-row/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findWords(words)
    print("\noutput:", serialize(ans, "string[]"))
