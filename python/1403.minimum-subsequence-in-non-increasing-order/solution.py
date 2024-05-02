# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        sub_sum = 0
        result = []

        for num in nums:
            sub_sum += num
            result.append(num)
            if sub_sum > total_sum - sub_sum:
                return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubsequence(nums)
    print("\noutput:", serialize(ans, "integer[]"))
