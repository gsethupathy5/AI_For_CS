# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

# @lc code=end

if __name__ == "__main__":
    orders: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().displayTable(orders)
    print("\noutput:", serialize(ans, "string[][]"))
