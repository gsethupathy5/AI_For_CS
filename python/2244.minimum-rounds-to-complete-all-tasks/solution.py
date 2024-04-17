# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRounds(tasks)
    print("\noutput:", serialize(ans, "integer"))
