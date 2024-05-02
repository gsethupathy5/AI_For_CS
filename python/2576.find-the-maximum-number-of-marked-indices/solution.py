# Created by asetti2002 at 2024/05/01 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        marked = 0
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if 2 * nums[i] <= nums[j]:
                marked += 1
                i += 1
                j -= 1
            else:
                j -= 1
        
        return marked
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumOfMarkedIndices(nums)
    print("\noutput:", serialize(ans, "integer"))
