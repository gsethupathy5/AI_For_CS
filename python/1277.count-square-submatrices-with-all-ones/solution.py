# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    count += 1
        
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    count += dp[i][j]
        
        return count
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countSquares(matrix)
    print("\noutput:", serialize(ans, "integer"))
