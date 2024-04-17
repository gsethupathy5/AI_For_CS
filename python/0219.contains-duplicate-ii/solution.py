# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().containsNearbyDuplicate(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
