# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countOrders(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countOrders(n)
    print("\noutput:", serialize(ans, "integer"))
