# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-groups-of-farmland/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    land: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findFarmland(land)
    print("\noutput:", serialize(ans, "integer[][]"))
