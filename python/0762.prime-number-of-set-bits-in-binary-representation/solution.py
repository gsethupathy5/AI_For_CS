# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().countPrimeSetBits(left, right)
    print("\noutput:", serialize(ans, "integer"))
