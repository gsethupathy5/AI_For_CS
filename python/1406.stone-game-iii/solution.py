# Created by asetti2002 at 2024/04/25 20:40
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # implementation of the stoneGameIII function
        pass
# @lc code=end

if __name__ == "__main__":
    stoneValue: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameIII(stoneValue)
    print("\noutput:", serialize(ans, "string"))
