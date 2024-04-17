# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/solve-the-equation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveEquation(self, equation: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    equation: str = deserialize("str", read_line())
    ans = Solution().solveEquation(equation)
    print("\noutput:", serialize(ans, "string"))
