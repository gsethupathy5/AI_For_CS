# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-two-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getSum(self, a: int, b: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().getSum(a, b)
    print("\noutput:", serialize(ans, "integer"))