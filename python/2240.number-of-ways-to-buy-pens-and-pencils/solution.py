# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    total: int = deserialize("int", read_line())
    cost1: int = deserialize("int", read_line())
    cost2: int = deserialize("int", read_line())
    ans = Solution().waysToBuyPensPencils(total, cost1, cost2)
    print("\noutput:", serialize(ans, "long"))
