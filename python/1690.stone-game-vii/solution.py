# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-vii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVII(stones)
    print("\noutput:", serialize(ans, "integer"))
