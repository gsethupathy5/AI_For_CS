# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/minesweeper/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    click: List[int] = deserialize("List[int]", read_line())
    ans = Solution().updateBoard(board, click)
    print("\noutput:", serialize(ans, "character[][]"))
