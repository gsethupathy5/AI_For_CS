# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/map-of-highest-peak/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    isWater: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().highestPeak(isWater)
    print("\noutput:", serialize(ans, "integer[][]"))
