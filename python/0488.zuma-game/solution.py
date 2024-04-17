# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/zuma-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    board: str = deserialize("str", read_line())
    hand: str = deserialize("str", read_line())
    ans = Solution().findMinStep(board, hand)
    print("\noutput:", serialize(ans, "integer"))
