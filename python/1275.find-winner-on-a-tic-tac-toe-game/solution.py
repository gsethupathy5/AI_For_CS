# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    moves: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().tictactoe(moves)
    print("\noutput:", serialize(ans, "string"))
