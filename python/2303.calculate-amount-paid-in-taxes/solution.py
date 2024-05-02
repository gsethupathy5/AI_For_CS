# Created by asetti2002 at 2024/04/25 20:23
# leetgo: 1.4.3
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        def calculate_tax(brackets, income):
            tax = 0.0
            for i in range(len(brackets)):
                if income > brackets[i][0]:
                    current_income = min(income, brackets[i][0]) - (brackets[i-1][0] if i > 0 else 0)
                    tax += current_income * brackets[i][1] / 100.0
            return tax

        return calculate_tax(brackets, income)
# @lc code=end

if __name__ == "__main__":
    brackets: List[List[int]] = deserialize("List[List[int]]", read_line())
    income: int = deserialize("int", read_line())
    ans = Solution().calculateTax(brackets, income)
    print("\noutput:", serialize(ans, "double"))
