# Created by asetti2002 at 2024/05/01 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-point-is-reachable/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        if targetX == targetY:
            return False
        while targetX > 1 and targetY > 1:
            if targetX > targetY:
                targetX %= targetY
            else:
                targetY %= targetX
        return (targetX == 1 and targetY == 1)
# @lc code=end

if __name__ == "__main__":
    targetX: int = deserialize("int", read_line())
    targetY: int = deserialize("int", read_line())
    ans = Solution().isReachable(targetX, targetY)
    print("\noutput:", serialize(ans, "boolean"))
