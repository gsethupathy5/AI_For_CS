# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(w1, w2):
            return sorted(w1) == sorted(w2)
        
        i = 1
        while i < len(words):
            if is_anagram(words[i-1], words[i]):
                words.pop(i)
            else:
                i += 1
        return words
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeAnagrams(words)
    print("\noutput:", serialize(ans, "string[]"))
