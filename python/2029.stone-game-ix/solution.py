# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-ix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameIX(stones)
    print("\noutput:", serialize(ans, "boolean"))
