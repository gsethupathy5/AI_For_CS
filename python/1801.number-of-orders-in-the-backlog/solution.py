# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-orders-in-the-backlog/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    orders: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getNumberOfBacklogOrders(orders)
    print("\noutput:", serialize(ans, "integer"))
