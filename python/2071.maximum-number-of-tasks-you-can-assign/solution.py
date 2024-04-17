# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    workers: List[int] = deserialize("List[int]", read_line())
    pills: int = deserialize("int", read_line())
    strength: int = deserialize("int", read_line())
    ans = Solution().maxTaskAssign(tasks, workers, pills, strength)
    print("\noutput:", serialize(ans, "integer"))
