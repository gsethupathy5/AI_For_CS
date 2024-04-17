# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/n-th-tribonacci-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def tribonacci(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().tribonacci(n)
    print("\noutput:", serialize(ans, "integer"))
