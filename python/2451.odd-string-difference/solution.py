# Created by asetti2002 at 2024/05/01 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/odd-string-difference/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = lambda word: [ord(word[i]) - ord(word[i-1]) for i in range(1, len(word))]
        unique_diff = list(set(diff(words[0])))
        for word in words:
            if unique_diff != diff(word):
                return word
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().oddString(words)
    print("\noutput:", serialize(ans, "string"))
