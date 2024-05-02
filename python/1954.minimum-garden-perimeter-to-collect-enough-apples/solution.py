# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def minimumPerimeter(self, neededApples: int) -> int:
            l, r = 0, 40000

            while l < r:
                m = (l + r) // 2
                if m ** 2 * (m + 1) ** 2 * 2 >= neededApples * 4:
                    r = m
                else:
                    l = m + 1
            
            return r * 8
# @lc code=end

if __name__ == "__main__":
    neededApples: int = deserialize("int", read_line())
    ans = Solution().minimumPerimeter(neededApples)
    print("\noutput:", serialize(ans, "long"))
