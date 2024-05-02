# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-area-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minAreaRect(points)
    print("\noutput:", serialize(ans, "integer"))
