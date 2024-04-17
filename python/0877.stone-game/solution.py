# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGame(piles)
    print("\noutput:", serialize(ans, "boolean"))
