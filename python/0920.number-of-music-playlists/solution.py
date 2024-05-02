# Created by asetti2002 at 2024/04/25 19:40
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-music-playlists/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j - 1] * (n - j + 1)
                dp[i][j] += dp[i - 1][j] * max(j - k, 0)
                dp[i][j] %= MOD
        return dp[goal][n]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    goal: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numMusicPlaylists(n, goal, k)
    print("\noutput:", serialize(ans, "integer"))
