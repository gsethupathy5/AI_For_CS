# Created by asetti2002 at 2024/05/01 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        pass
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxPoints(grid, queries)
    print("\noutput:", serialize(ans, "integer[]"))
