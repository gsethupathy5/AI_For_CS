# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/course-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))
