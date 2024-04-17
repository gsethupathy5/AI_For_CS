# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    divisor1: int = deserialize("int", read_line())
    divisor2: int = deserialize("int", read_line())
    uniqueCnt1: int = deserialize("int", read_line())
    uniqueCnt2: int = deserialize("int", read_line())
    ans = Solution().minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    print("\noutput:", serialize(ans, "integer"))
