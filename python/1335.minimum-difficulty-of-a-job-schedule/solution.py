# Created by asetti2002 at 2024/04/25 20:32
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n, inf = len(jobDifficulty), float('inf')
        if n < d:
            return -1

        dp = [[inf] * n for _ in range(d + 1)]
        dp[0][0] = jobDifficulty[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])

        for i in range(1, d):
            for j in range(i, n):
                max_d = 0
                for k in range(j, i - 1, -1):
                    max_d = max(max_d, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + max_d)

        return dp[d - 1][n - 1]
# @lc code=end

if __name__ == "__main__":
    jobDifficulty: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().minDifficulty(jobDifficulty, d)
    print("\noutput:", serialize(ans, "integer"))
