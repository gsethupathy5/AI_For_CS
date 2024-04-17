# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/concatenated-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findAllConcatenatedWordsInADict(words)
    print("\noutput:", serialize(ans, "string[]"))
