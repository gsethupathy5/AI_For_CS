# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-1-bits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hammingWeight(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().hammingWeight(n)
    print("\noutput:", serialize(ans, "integer"))
