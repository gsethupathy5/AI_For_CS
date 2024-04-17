# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().rangeBitwiseAnd(left, right)
    print("\noutput:", serialize(ans, "integer"))
