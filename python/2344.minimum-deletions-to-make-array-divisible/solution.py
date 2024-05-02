# Created by asetti2002 at 2024/05/01 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        lcm_num = nums[0]
        for num in nums[1:]:
            lcm_num = lcm(lcm_num, num)

        gcd_num = numsDivide[0]
        for num in numsDivide[1:]:
            gcd_num = gcd(gcd_num, num)

        if gcd_num % lcm_num != 0:
            return -1

        count = 0
        for num in nums:
            temp_lcm_num = lcm_num // gcd(lcm_num, num)
            if gcd_num % temp_lcm_num != 0:
                count += 1

        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    numsDivide: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums, numsDivide)
    print("\noutput:", serialize(ans, "integer"))
