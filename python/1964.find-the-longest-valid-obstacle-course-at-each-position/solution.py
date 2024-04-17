# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    obstacles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestObstacleCourseAtEachPosition(obstacles)
    print("\noutput:", serialize(ans, "integer[]"))
