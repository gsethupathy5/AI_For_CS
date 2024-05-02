# Created by asetti2002 at 2024/05/01 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def has_common_divisor(arr):
            common = arr[0]
            for num in arr:
                common = gcd(common, num)
                if common == k:
                    return True
            return False
        
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if has_common_divisor(nums[i:j+1]):
                    count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarrayGCD(nums, k)
    print("\noutput:", serialize(ans, "integer"))
