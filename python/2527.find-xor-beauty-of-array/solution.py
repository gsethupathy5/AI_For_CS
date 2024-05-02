# Created by asetti2002 at 2024/05/01 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/find-xor-beauty-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    result ^= ((nums[i]|nums[j]) & nums[k])
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().xorBeauty(nums)
    print("\noutput:", serialize(ans, "integer"))
