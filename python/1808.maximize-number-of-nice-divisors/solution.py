# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-number-of-nice-divisors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    primeFactors: int = deserialize("int", read_line())
    ans = Solution().maxNiceDivisors(primeFactors)
    print("\noutput:", serialize(ans, "integer"))
