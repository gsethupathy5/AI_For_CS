# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    letters: List[str] = deserialize("List[str]", read_line())
    score: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScoreWords(words, letters, score)
    print("\noutput:", serialize(ans, "integer"))
