# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/coordinate-with-maximum-network-quality/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    towers: List[List[int]] = deserialize("List[List[int]]", read_line())
    radius: int = deserialize("int", read_line())
    ans = Solution().bestCoordinate(towers, radius)
    print("\noutput:", serialize(ans, "integer[]"))
