# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/grumpy-bookstore-owner/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])
        max_additional = 0
        additional = sum([customers[i] for i in range(minutes) if grumpy[i] == 1])
        max_additional = additional
        for i in range(minutes, len(customers)):
            additional = additional + customers[i]*grumpy[i] - customers[i-minutes]*grumpy[i-minutes]
            max_additional = max(max_additional, additional)
        
        return satisfied + max_additional
# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    grumpy: List[int] = deserialize("List[int]", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().maxSatisfied(customers, grumpy, minutes)
    print("\noutput:", serialize(ans, "integer"))
