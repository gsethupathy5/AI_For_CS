# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameII(piles)
    print("\noutput:", serialize(ans, "integer"))
