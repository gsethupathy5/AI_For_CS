# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/basic-calculator-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    expression: str = deserialize("str", read_line())
    evalvars: List[str] = deserialize("List[str]", read_line())
    evalints: List[int] = deserialize("List[int]", read_line())
    ans = Solution().basicCalculatorIV(expression, evalvars, evalints)
    print("\noutput:", serialize(ans, "string[]"))
