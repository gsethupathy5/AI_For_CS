# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/game-of-life/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    gameOfLife(board)
    ans = board
    print("\noutput:", serialize(ans, "List[List[int]]"))
