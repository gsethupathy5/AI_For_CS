# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    chargeTimes: List[int] = deserialize("List[int]", read_line())
    runningCosts: List[int] = deserialize("List[int]", read_line())
    budget: int = deserialize("int", read_line())
    ans = Solution().maximumRobots(chargeTimes, runningCosts, budget)
    print("\noutput:", serialize(ans, "integer"))
