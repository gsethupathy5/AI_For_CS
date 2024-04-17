# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().concatenatedBinary(n)
    print("\noutput:", serialize(ans, "integer"))
