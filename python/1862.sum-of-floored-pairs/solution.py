# Created by asetti2002 at 2024/04/25 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-floored-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        count = [0] * (max_num + 1)
        
        for num in nums:
            count[num] += 1
        
        prefix_sum = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sum[i] = prefix_sum[i - 1] + count[i]
        
        result = 0
        for i in range(len(nums)):
            for j in range(1, max_num // nums[i] + 1):
                num = j * nums[i]
                result += count[j] * (prefix_sum[min(max_num, num + nums[i] - 1)] - prefix_sum[num - 1])
        
        return result % MOD
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumOfFlooredPairs(nums)
    print("\noutput:", serialize(ans, "integer"))
