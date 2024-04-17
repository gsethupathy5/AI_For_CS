# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/out-of-boundary-paths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    maxMove: int = deserialize("int", read_line())
    startRow: int = deserialize("int", read_line())
    startColumn: int = deserialize("int", read_line())
    ans = Solution().findPaths(m, n, maxMove, startRow, startColumn)
    print("\noutput:", serialize(ans, "integer"))
