# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numMovesStonesII(stones)
    print("\noutput:", serialize(ans, "integer[]"))
