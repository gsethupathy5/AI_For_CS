# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getBiggestThree(grid)
    print("\noutput:", serialize(ans, "integer[]"))
