# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/sudoku-solver/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    solveSudoku(board)
    ans = board
    print("\noutput:", serialize(ans, "List[List[str]]"))
