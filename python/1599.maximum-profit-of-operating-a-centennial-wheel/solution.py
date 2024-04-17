# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    boardingCost: int = deserialize("int", read_line())
    runningCost: int = deserialize("int", read_line())
    ans = Solution().minOperationsMaxProfit(customers, boardingCost, runningCost)
    print("\noutput:", serialize(ans, "integer"))
