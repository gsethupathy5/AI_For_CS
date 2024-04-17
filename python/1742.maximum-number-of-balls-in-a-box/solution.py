# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    lowLimit: int = deserialize("int", read_line())
    highLimit: int = deserialize("int", read_line())
    ans = Solution().countBalls(lowLimit, highLimit)
    print("\noutput:", serialize(ans, "integer"))
