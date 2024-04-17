# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().hammingDistance(x, y)
    print("\noutput:", serialize(ans, "integer"))
