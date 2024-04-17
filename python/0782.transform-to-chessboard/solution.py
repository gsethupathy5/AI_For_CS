# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/transform-to-chessboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().movesToChessboard(board)
    print("\noutput:", serialize(ans, "integer"))
