# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/categorize-box-according-to-criteria/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    length: int = deserialize("int", read_line())
    width: int = deserialize("int", read_line())
    height: int = deserialize("int", read_line())
    mass: int = deserialize("int", read_line())
    ans = Solution().categorizeBox(length, width, height, mass)
    print("\noutput:", serialize(ans, "string"))
