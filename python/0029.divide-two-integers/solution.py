# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-two-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    dividend: int = deserialize("int", read_line())
    divisor: int = deserialize("int", read_line())
    ans = Solution().divide(dividend, divisor)
    print("\noutput:", serialize(ans, "integer"))
