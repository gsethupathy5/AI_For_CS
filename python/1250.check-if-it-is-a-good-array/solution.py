# Created by asetti2002 at 2024/04/25 20:22
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-it-is-a-good-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        g = nums[0]
        for num in nums[1:]:
            g = gcd(g, num)
            if g == 1:
                return True
        return False
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isGoodArray(nums)
    print("\noutput:", serialize(ans, "boolean"))
