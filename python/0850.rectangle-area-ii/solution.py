# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/rectangle-area-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        event = []
        for x1, y1, x2, y2 in rectangles:
            event.append((y1, 1, x1, x2))
            event.append((y2, -1, x1, x2))
        event.sort()
        active = []
        cur_y = cur_x_sum = area = 0
        for y, typ, x1, x2 in event:
            area += (y - cur_y) * cur_x_sum
            cur_x_sum = self.update(active, x1, x2, typ)
            cur_y = y
        return area % MOD
    
    def update(self, active, x1, x2, typ):
        new_active = []
        cur_x_sum = 0
        for x1_, x2_ in active:
            if x1 >= x2_ or x2 <= x1_:
                new_active.append((x1_, x2_))
            else:
                cur_x_sum += x2_ - x1_
                new_active.append((min(x1, x1_), max(x2, x2_)))
        active[:] = new_active
        if typ == 1:
            active.append((x1, x2))
            cur_x_sum += x2 - x1
        return cur_x_sum
# @lc code=end

if __name__ == "__main__":
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().rectangleArea(rectangles)
    print("\noutput:", serialize(ans, "integer"))
