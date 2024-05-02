# Created by asetti2002 at 2024/04/25 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        result = 0
        first_max = 0
        second_max = 0
        
        for i in range(firstLen, len(nums) - secondLen + 1):
            first_max = max(first_max, prefix_sum[i] - prefix_sum[i - firstLen])
            second_max = max(second_max, prefix_sum[i + secondLen] - prefix_sum[i])
            result = max(result, first_max + prefix_sum[i + secondLen] - prefix_sum[i])
        
        first_max = 0
        second_max = 0
        
        for i in range(secondLen, len(nums) - firstLen + 1):
            first_max = max(first_max, prefix_sum[i] - prefix_sum[i - secondLen])
            second_max = max(second_max, prefix_sum[i + firstLen] - prefix_sum[i])
            result = max(result, first_max + prefix_sum[i + firstLen] - prefix_sum[i])
        
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    firstLen: int = deserialize("int", read_line())
    secondLen: int = deserialize("int", read_line())
    ans = Solution().maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print("\noutput:", serialize(ans, "integer"))
