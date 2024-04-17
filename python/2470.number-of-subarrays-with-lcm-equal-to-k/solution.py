# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarrayLCM(nums, k)
    print("\noutput:", serialize(ans, "integer"))
