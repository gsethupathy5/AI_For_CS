# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/stone-game-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().winnerSquareGame(n)
    print("\noutput:", serialize(ans, "boolean"))
