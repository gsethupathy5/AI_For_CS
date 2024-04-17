# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/knight-probability-in-chessboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    row: int = deserialize("int", read_line())
    column: int = deserialize("int", read_line())
    ans = Solution().knightProbability(n, k, row, column)
    print("\noutput:", serialize(ans, "double"))
