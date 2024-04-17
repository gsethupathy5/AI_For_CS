# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    headID: int = deserialize("int", read_line())
    manager: List[int] = deserialize("List[int]", read_line())
    informTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numOfMinutes(n, headID, manager, informTime)
    print("\noutput:", serialize(ans, "integer"))
