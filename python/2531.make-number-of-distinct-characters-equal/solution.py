# Created by asetti2002 at 2024/05/01 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        if abs(len(set(word1)) - len(set(word2))) != 1:
            return False
        for i, char1 in enumerate(word1):
            for j, char2 in enumerate(word2):
                if len(set(word1[:i] + [char2] + word1[i+1:])) == len(set(word2[:j] + [char1] + word2[j+1:])):
                    return True
        return False
# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().isItPossible(word1, word2)
    print("\noutput:", serialize(ans, "boolean"))
