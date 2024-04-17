# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/the-skyline-problem/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    buildings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getSkyline(buildings)
    print("\noutput:", serialize(ans, "integer[][]"))
