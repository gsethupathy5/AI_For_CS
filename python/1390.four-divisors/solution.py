# Created by asetti2002 at 2024/04/25 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/four-divisors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(num):
            count = 0
            total = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 2
                    total += i
                    if i != num // i:
                        total += num // i
                if count > 4:
                    return 0
            return total if count == 4 else 0
        
        result = 0
        for num in nums:
            result += divisors(num)
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumFourDivisors(nums)
    print("\noutput:", serialize(ans, "integer"))
