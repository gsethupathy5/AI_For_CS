# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/add-minimum-number-of-rungs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    rungs: List[int] = deserialize("List[int]", read_line())
    dist: int = deserialize("int", read_line())
    ans = Solution().addRungs(rungs, dist)
    print("\noutput:", serialize(ans, "integer"))
