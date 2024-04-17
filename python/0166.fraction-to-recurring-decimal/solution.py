# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/fraction-to-recurring-decimal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    numerator: int = deserialize("int", read_line())
    denominator: int = deserialize("int", read_line())
    ans = Solution().fractionToDecimal(numerator, denominator)
    print("\noutput:", serialize(ans, "string"))
