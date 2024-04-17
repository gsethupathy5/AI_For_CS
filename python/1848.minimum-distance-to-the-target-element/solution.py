# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-distance-to-the-target-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().getMinDistance(nums, target, start)
    print("\noutput:", serialize(ans, "integer"))
