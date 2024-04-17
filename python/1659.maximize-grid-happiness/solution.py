# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-grid-happiness/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    introvertsCount: int = deserialize("int", read_line())
    extrovertsCount: int = deserialize("int", read_line())
    ans = Solution().getMaxGridHappiness(m, n, introvertsCount, extrovertsCount)
    print("\noutput:", serialize(ans, "integer"))
