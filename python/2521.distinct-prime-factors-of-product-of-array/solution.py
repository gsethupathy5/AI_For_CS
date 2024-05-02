# Created by asetti2002 at 2024/05/01 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        from collections import Counter
        from sympy import factorint
        
        prime_factors = Counter()
        for num in nums:
            factors = factorint(num)
            for factor in factors.keys():
                prime_factors[factor] += 1
        
        return len(prime_factors)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distinctPrimeFactors(nums)
    print("\noutput:", serialize(ans, "integer"))
