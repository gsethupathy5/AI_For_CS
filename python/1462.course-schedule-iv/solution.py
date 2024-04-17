# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/course-schedule-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkIfPrerequisite(numCourses, prerequisites, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
