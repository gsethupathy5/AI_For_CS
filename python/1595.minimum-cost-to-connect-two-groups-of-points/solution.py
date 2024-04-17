# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    cost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().connectTwoGroups(cost)
    print("\noutput:", serialize(ans, "integer"))
