# Created by asetti2002 at 2024/04/25 20:40
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007
        a = b = 6
        for i in range(1, n):
            a, b = (2 * a + 2 * b) % mod, (2 * a + 3 * b) % mod
        return (a + b) % mod
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numOfWays(n)
    print("\noutput:", serialize(ans, "integer"))
