# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/course-schedule-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    courses: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().scheduleCourse(courses)
    print("\noutput:", serialize(ans, "integer"))
