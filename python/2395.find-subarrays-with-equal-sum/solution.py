# Created by asetti2002 at 2024/05/01 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        seen = {}
        for i in range(len(nums) - 1):
            for j in range(i + 2, len(nums)): 
                current_sum = prefix_sum[j + 1] - prefix_sum[i]
                if current_sum in seen:
                    return True
                seen[current_sum] = (i, j)
        
        return False
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findSubarrays(nums)
    print("\noutput:", serialize(ans, "boolean"))
