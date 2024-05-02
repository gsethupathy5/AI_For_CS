# Created by asetti2002 at 2024/05/01 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-nice-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check_bitwise_and_zero(num1, num2):
            return num1 & num2 == 0
        
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if all(check_bitwise_and_zero(nums[k], nums[l]) for k in range(i, j) for l in range(k+1, j)):
                    max_len = max(max_len, j-i+1)
        
        return max_len
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestNiceSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
