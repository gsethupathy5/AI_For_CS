# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/bricks-falling-when-hit/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    hits: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().hitBricks(grid, hits)
    print("\noutput:", serialize(ans, "integer[]"))
