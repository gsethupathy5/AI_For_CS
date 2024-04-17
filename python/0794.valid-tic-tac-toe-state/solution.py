# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-tic-tac-toe-state/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    board: List[str] = deserialize("List[str]", read_line())
    ans = Solution().validTicTacToe(board)
    print("\noutput:", serialize(ans, "boolean"))
