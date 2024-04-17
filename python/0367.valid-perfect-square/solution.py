# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-perfect-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().isPerfectSquare(num)
    print("\noutput:", serialize(ans, "boolean"))
