# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfWays(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numOfWays(n)
    print("\noutput:", serialize(ans, "integer"))
