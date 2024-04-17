# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/spiral-matrix-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    rows: int = deserialize("int", read_line())
    cols: int = deserialize("int", read_line())
    rStart: int = deserialize("int", read_line())
    cStart: int = deserialize("int", read_line())
    ans = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
    print("\noutput:", serialize(ans, "integer[][]"))
