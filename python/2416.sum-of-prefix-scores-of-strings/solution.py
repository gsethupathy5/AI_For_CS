# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().sumPrefixScores(words)
    print("\noutput:", serialize(ans, "integer[]"))
