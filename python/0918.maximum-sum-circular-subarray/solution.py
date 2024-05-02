# Created by asetti2002 at 2024/04/25 19:39
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)

        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubarraySumCircular(nums)
    print("\noutput:", serialize(ans, "integer"))
