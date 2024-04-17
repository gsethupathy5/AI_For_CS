# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    position: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostToMoveChips(position)
    print("\noutput:", serialize(ans, "integer"))
