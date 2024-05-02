# Created by asetti2002 at 2024/05/01 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        pairs = {}
        max_sum = -1

        for i, num in enumerate(nums):
            digit_sum_num = digit_sum(num)
            if digit_sum_num in pairs:
                pair_index = pairs[digit_sum_num]
                pair_sum = nums[pair_index] + num
                if pair_sum > max_sum:
                    max_sum = pair_sum
            else:
                pairs[digit_sum_num] = i

        return max_sum
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(nums)
    print("\noutput:", serialize(ans, "integer"))
