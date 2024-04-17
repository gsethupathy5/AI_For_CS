# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/champagne-tower/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    poured: int = deserialize("int", read_line())
    query_row: int = deserialize("int", read_line())
    query_glass: int = deserialize("int", read_line())
    ans = Solution().champagneTower(poured, query_row, query_glass)
    print("\noutput:", serialize(ans, "double"))
