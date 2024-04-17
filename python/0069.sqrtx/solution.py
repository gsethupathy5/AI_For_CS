# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/sqrtx/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mySqrt(self, x: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().mySqrt(x)
    print("\noutput:", serialize(ans, "integer"))
