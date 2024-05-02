# Created by asetti2002 at 2024/04/25 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/closest-divisors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_divisors(n):
            for i in range(int(n ** 0.5), 0, -1):
                if n % i == 0:
                    return i, n // i
        
        diff1 = abs(num + 1 - 1)
        diff2 = abs(num + 2 - 1)
        
        divisors1 = find_divisors(num + 1)
        divisors2 = find_divisors(num + 2)
        
        if diff1 < diff2:
            return [divisors1]
        else:
            return [divisors2]
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().closestDivisors(num)
    print("\noutput:", serialize(ans, "integer[]"))
