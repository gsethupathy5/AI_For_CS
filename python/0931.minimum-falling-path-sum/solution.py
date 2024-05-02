# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0, j-1):min(n, j+2)])
        return min(matrix[-1])
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(matrix)
    print("\noutput:", serialize(ans, "integer"))
