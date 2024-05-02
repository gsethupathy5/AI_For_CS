# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                result ^= num1 ^ num2
        return result
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().xorAllNums(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
