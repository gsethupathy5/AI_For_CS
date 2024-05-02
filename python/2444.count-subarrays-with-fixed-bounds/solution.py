# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        ans = 0
        left = 0
        
        for right in range(len(nums)):
            if minK <= nums[right] <= maxK:
                count = right - left + 1
                ans += count
            else:
                count = 0
                left = right + 1
        
        return ans
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    minK: int = deserialize("int", read_line())
    maxK: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, minK, maxK)
    print("\noutput:", serialize(ans, "long"))
