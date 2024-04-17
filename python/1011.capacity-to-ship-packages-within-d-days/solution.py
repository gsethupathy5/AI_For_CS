# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    weights: List[int] = deserialize("List[int]", read_line())
    days: int = deserialize("int", read_line())
    ans = Solution().shipWithinDays(weights, days)
    print("\noutput:", serialize(ans, "integer"))
