# Created by asetti2002 at 2024/05/01 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        prefix_product = [1]
        for num in nums:
            prefix_product.append(prefix_product[-1] * num)
            
        suffix_product = [1]
        for num in reversed(nums):
            suffix_product.insert(0, suffix_product[0] * num)
            
        for i in range(len(nums) - 1):
            if gcd(prefix_product[i + 1], suffix_product[i]) == 1:
                return i
        return -1
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findValidSplit(nums)
    print("\noutput:", serialize(ans, "integer"))
