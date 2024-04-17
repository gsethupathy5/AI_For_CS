# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-paths-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    obstacleGrid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsWithObstacles(obstacleGrid)
    print("\noutput:", serialize(ans, "integer"))
