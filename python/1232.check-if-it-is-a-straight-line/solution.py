# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y1 - y0) * (x - x0) != (x1 - x0) * (y - y0):
                return False
        
        return True
# @lc code=end

if __name__ == "__main__":
    coordinates: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkStraightLine(coordinates)
    print("\noutput:", serialize(ans, "boolean"))
