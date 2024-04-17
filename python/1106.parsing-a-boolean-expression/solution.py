# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/parsing-a-boolean-expression/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    ans = Solution().parseBoolExpr(expression)
    print("\noutput:", serialize(ans, "boolean"))
