# Created by asetti2002 at 2024/04/25 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            curr = capacity
            required_days = 1
            for weight in weights:
                if weight > curr:
                    required_days += 1
                    curr = capacity
                curr -= weight
            return required_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

if __name__ == "__main__":
    weights: List[int] = deserialize("List[int]", read_line())
    days: int = deserialize("int", read_line())
    ans = Solution().shipWithinDays(weights, days)
    print("\noutput:", serialize(ans, "integer"))
