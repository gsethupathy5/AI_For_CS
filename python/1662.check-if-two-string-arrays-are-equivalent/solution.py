# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    word1: List[str] = deserialize("List[str]", read_line())
    word2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().arrayStringsAreEqual(word1, word2)
    print("\noutput:", serialize(ans, "boolean"))
