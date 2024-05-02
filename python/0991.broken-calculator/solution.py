# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/broken-calculator/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
        return res + startValue - target
# @lc code=end

if __name__ == "__main__":
    startValue: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().brokenCalc(startValue, target)
    print("\noutput:", serialize(ans, "integer"))
