# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-number-with-alternating-bits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().hasAlternatingBits(n)
    print("\noutput:", serialize(ans, "boolean"))
