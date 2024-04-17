# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/trapping-rain-water-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    heightMap: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().trapRainWater(heightMap)
    print("\noutput:", serialize(ans, "integer"))
