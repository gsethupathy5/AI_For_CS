# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().onesMinusZeros(grid)
    print("\noutput:", serialize(ans, "integer[][]"))
