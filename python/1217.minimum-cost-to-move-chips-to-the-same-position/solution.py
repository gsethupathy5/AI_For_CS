# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for pos in position:
            if pos % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
# @lc code=end

if __name__ == "__main__":
    position: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCostToMoveChips(position)
    print("\noutput:", serialize(ans, "integer"))
