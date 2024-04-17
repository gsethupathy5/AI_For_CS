# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/reverse-bits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverseBits(self, n: int) -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: str = deserialize("str", read_line())
    ans = Solution().reverseBits(n)
    print("\noutput:", serialize(ans, "integer"))
