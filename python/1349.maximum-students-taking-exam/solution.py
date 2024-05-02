# Created by asetti2002 at 2024/04/25 20:33
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-students-taking-exam/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    seats: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maxStudents(seats)
    print("\noutput:", serialize(ans, "integer"))
