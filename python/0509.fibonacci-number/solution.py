# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/fibonacci-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().fib(n)
    print("\noutput:", serialize(ans, "integer"))
