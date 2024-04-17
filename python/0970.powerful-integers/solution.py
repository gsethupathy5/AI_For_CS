# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/powerful-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    bound: int = deserialize("int", read_line())
    ans = Solution().powerfulIntegers(x, y, bound)
    print("\noutput:", serialize(ans, "integer[]"))
