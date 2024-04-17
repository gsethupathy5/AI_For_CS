# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/matrix-cells-in-distance-order/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    rows: int = deserialize("int", read_line())
    cols: int = deserialize("int", read_line())
    rCenter: int = deserialize("int", read_line())
    cCenter: int = deserialize("int", read_line())
    ans = Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)
    print("\noutput:", serialize(ans, "integer[][]"))
