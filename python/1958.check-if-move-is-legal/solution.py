# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-move-is-legal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    rMove: int = deserialize("int", read_line())
    cMove: int = deserialize("int", read_line())
    color: str = deserialize("str", read_line())
    ans = Solution().checkMove(board, rMove, cMove, color)
    print("\noutput:", serialize(ans, "boolean"))
