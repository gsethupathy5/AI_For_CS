# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-pairs-of-similar-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().similarPairs(words)
    print("\noutput:", serialize(ans, "integer"))
