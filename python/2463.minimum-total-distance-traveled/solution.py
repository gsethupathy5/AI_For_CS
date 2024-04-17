# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-total-distance-traveled/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    robot: List[int] = deserialize("List[int]", read_line())
    factory: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotalDistance(robot, factory)
    print("\noutput:", serialize(ans, "long"))
