# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    brackets: List[List[int]] = deserialize("List[List[int]]", read_line())
    income: int = deserialize("int", read_line())
    ans = Solution().calculateTax(brackets, income)
    print("\noutput:", serialize(ans, "double"))
