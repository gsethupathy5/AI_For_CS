# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/broken-calculator/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startValue: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().brokenCalc(startValue, target)
    print("\noutput:", serialize(ans, "integer"))
