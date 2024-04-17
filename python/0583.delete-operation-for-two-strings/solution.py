# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-operation-for-two-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))
