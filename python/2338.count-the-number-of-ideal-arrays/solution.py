# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    maxValue: int = deserialize("int", read_line())
    ans = Solution().idealArrays(n, maxValue)
    print("\noutput:", serialize(ans, "integer"))
