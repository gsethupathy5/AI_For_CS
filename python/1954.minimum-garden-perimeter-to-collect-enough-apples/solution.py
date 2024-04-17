# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    neededApples: int = deserialize("int", read_line())
    ans = Solution().minimumPerimeter(neededApples)
    print("\noutput:", serialize(ans, "long"))
