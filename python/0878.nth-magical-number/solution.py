# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/nth-magical-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().nthMagicalNumber(n, a, b)
    print("\noutput:", serialize(ans, "integer"))