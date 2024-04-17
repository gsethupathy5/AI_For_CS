# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/super-ugly-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    primes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().nthSuperUglyNumber(n, primes)
    print("\noutput:", serialize(ans, "integer"))
