# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    days: List[int] = deserialize("List[int]", read_line())
    costs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mincostTickets(days, costs)
    print("\noutput:", serialize(ans, "integer"))
