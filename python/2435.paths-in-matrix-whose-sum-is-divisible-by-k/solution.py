# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfPaths(grid, k)
    print("\noutput:", serialize(ans, "integer"))
