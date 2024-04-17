# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minimumOneBitOperations(n)
    print("\noutput:", serialize(ans, "integer"))
