# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/ugly-number-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().nthUglyNumber(n, a, b, c)
    print("\noutput:", serialize(ans, "integer"))
