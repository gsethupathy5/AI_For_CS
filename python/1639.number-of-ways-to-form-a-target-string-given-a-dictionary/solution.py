# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().numWays(words, target)
    print("\noutput:", serialize(ans, "integer"))
