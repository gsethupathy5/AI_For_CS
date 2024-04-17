# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    types: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().waysToReachTarget(target, types)
    print("\noutput:", serialize(ans, "integer"))
