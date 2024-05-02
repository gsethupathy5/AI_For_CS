# Created by asetti2002 at 2024/04/25 20:25
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-visiting-all-points/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i - 1][0])
            y_diff = abs(points[i][1] - points[i - 1][1])
            time += max(x_diff, y_diff)
        return time
# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTimeToVisitAllPoints(points)
    print("\noutput:", serialize(ans, "integer"))
