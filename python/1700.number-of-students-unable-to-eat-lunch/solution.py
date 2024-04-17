# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    students: List[int] = deserialize("List[int]", read_line())
    sandwiches: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countStudents(students, sandwiches)
    print("\noutput:", serialize(ans, "integer"))
