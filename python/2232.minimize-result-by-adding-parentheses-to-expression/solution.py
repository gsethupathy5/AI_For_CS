# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizeResult(self, expression: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    ans = Solution().minimizeResult(expression)
    print("\noutput:", serialize(ans, "string"))