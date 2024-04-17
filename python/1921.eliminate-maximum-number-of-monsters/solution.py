# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().eliminateMaximum(dist, speed)
    print("\noutput:", serialize(ans, "integer"))
