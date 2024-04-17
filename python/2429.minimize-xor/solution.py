# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-xor/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num1: int = deserialize("int", read_line())
    num2: int = deserialize("int", read_line())
    ans = Solution().minimizeXor(num1, num2)
    print("\noutput:", serialize(ans, "integer"))
