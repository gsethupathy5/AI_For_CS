# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    sentences: List[str] = deserialize("List[str]", read_line())
    ans = Solution().mostWordsFound(sentences)
    print("\noutput:", serialize(ans, "integer"))
