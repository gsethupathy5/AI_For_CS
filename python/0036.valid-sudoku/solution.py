# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-sudoku/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().isValidSudoku(board)
    print("\noutput:", serialize(ans, "boolean"))
