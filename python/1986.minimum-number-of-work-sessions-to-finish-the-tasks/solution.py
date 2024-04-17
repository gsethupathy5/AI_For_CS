# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    sessionTime: int = deserialize("int", read_line())
    ans = Solution().minSessions(tasks, sessionTime)
    print("\noutput:", serialize(ans, "integer"))
