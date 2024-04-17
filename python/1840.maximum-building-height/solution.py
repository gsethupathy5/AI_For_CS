# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-building-height/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    restrictions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxBuilding(n, restrictions)
    print("\noutput:", serialize(ans, "integer"))
