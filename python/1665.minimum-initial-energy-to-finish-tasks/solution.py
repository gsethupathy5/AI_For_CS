# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumEffort(tasks)
    print("\noutput:", serialize(ans, "integer"))
