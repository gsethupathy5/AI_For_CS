# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    searchWord: str = deserialize("str", read_line())
    ans = Solution().isPrefixOfWord(sentence, searchWord)
    print("\noutput:", serialize(ans, "integer"))
