# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
        
        if (x_y + y_x) % 2 != 0:
            return -1
        
        return x_y // 2 + y_x // 2 + x_y % 2 + y_x % 2
# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().minimumSwap(s1, s2)
    print("\noutput:", serialize(ans, "integer"))
