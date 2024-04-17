# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    queryTime: int = deserialize("int", read_line())
    ans = Solution().busyStudent(startTime, endTime, queryTime)
    print("\noutput:", serialize(ans, "integer"))
