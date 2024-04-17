# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/powx-n/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def myPow(self, x: float, n: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    x: float = deserialize("float", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().myPow(x, n)
    print("\noutput:", serialize(ans, "double"))
