# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/the-score-of-students-solving-math-expression/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    answers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().scoreOfStudents(s, answers)
    print("\noutput:", serialize(ans, "integer"))
