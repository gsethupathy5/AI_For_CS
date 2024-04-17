# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().pacificAtlantic(heights)
    print("\noutput:", serialize(ans, "integer[][]"))
