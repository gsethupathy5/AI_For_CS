# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    minK: int = deserialize("int", read_line())
    maxK: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, minK, maxK)
    print("\noutput:", serialize(ans, "long"))
