# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/average-waiting-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    customers: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().averageWaitingTime(customers)
    print("\noutput:", serialize(ans, "double"))
