# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    firstWord: str = deserialize("str", read_line())
    secondWord: str = deserialize("str", read_line())
    targetWord: str = deserialize("str", read_line())
    ans = Solution().isSumEqual(firstWord, secondWord, targetWord)
    print("\noutput:", serialize(ans, "boolean"))
