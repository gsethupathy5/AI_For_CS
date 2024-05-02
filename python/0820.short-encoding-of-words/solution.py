# Created by asetti2002 at 2024/04/25 19:07
# leetgo: 1.4.3
# https://leetcode.com/problems/short-encoding-of-words/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])
        return sum(len(word) + 1 for word in word_set)
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minimumLengthEncoding(words)
    print("\noutput:", serialize(ans, "integer"))
