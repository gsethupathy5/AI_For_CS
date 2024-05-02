# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    cuboids: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxHeight(cuboids)
    print("\noutput:", serialize(ans, "integer"))
