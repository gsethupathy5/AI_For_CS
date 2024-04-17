# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().closestPrimes(left, right)
    print("\noutput:", serialize(ans, "integer[]"))
