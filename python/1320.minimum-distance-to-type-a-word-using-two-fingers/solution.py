# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumDistance(self, word: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().minimumDistance(word)
    print("\noutput:", serialize(ans, "integer"))
