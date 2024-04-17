# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    inventory: List[int] = deserialize("List[int]", read_line())
    orders: int = deserialize("int", read_line())
    ans = Solution().maxProfit(inventory, orders)
    print("\noutput:", serialize(ans, "integer"))
