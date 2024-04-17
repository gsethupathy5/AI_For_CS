# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().findMinFibonacciNumbers(k)
    print("\noutput:", serialize(ans, "integer"))
