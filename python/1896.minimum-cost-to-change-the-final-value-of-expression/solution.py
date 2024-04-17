# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    ans = Solution().minOperationsToFlip(expression)
    print("\noutput:", serialize(ans, "integer"))
