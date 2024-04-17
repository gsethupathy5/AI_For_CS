# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/best-position-for-a-service-centre/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    positions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getMinDistSum(positions)
    print("\noutput:", serialize(ans, "double"))
