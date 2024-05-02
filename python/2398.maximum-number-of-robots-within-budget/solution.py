# Created by asetti2002 at 2024/05/01 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        max_robots = 0
        for i in range(len(chargeTimes)):
            total_cost = max(chargeTimes[:i+1]) + (i+1) * sum(runningCosts[:i+1])
            if total_cost <= budget:
                max_robots = i + 1
            else:
                break
        return max_robots
# @lc code=end

if __name__ == "__main__":
    chargeTimes: List[int] = deserialize("List[int]", read_line())
    runningCosts: List[int] = deserialize("List[int]", read_line())
    budget: int = deserialize("int", read_line())
    ans = Solution().maximumRobots(chargeTimes, runningCosts, budget)
    print("\noutput:", serialize(ans, "integer"))
