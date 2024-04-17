# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/xor-operation-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().xorOperation(n, start)
    print("\noutput:", serialize(ans, "integer"))
