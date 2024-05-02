# Created by asetti2002 at 2024/04/25 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {c: i for i, c in enumerate(order)}
        
        def compare_words(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if alien_dict[word1[i]] < alien_dict[word2[i]]:
                    return -1
                elif alien_dict[word1[i]] > alien_dict[word2[i]]:
                    return 1
                i += 1
            return -1 if len(word1) < len(word2) else 0
        
        for i in range(1, len(words)):
            if compare_words(words[i-1], words[i]) > 0:
                return False
        
        return True
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    order: str = deserialize("str", read_line())
    ans = Solution().isAlienSorted(words, order)
    print("\noutput:", serialize(ans, "boolean"))
