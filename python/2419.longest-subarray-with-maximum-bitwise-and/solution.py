# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_bitwise_and = 0
        bitwise_and = 0
        count = 0
        
        for num in nums:
            max_bitwise_and = max(max_bitwise_and, num)
            bitwise_and &= num
            if bitwise_and == max_bitwise_and:
                count += 1
            else:
                count = 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
