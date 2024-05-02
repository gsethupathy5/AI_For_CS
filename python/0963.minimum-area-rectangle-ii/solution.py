# Created by asetti2002 at 2024/04/25 19:46
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-area-rectangle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        pass
# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minAreaFreeRect(points)
    print("\noutput:", serialize(ans, "double"))
