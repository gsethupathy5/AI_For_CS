# Created by asetti2002 at 2024/04/25 19:35
# leetgo: 1.4.3
# https://leetcode.com/problems/spiral-matrix-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        length = 0
        
        while len(res) < rows * cols:
            if direction == 0 or direction == 2:
                length += 1
            for _ in range(length):
                rStart += dirs[direction][0]
                cStart += dirs[direction][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            
            direction = (direction + 1) % 4
        return res
# @lc code=end

if __name__ == "__main__":
    rows: int = deserialize("int", read_line())
    cols: int = deserialize("int", read_line())
    rStart: int = deserialize("int", read_line())
    cStart: int = deserialize("int", read_line())
    ans = Solution().spiralMatrixIII(rows, cols, rStart, cStart)
    print("\noutput:", serialize(ans, "integer[][]"))
