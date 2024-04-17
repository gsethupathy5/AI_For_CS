# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/contains-duplicate-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    indexDiff: int = deserialize("int", read_line())
    valueDiff: int = deserialize("int", read_line())
    ans = Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
    print("\noutput:", serialize(ans, "boolean"))
