# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumSubarraySum(nums, k)
    print("\noutput:", serialize(ans, "long"))
