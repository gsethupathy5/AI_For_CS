# Created by asetti2002 at 2024/04/25 19:03
# leetgo: 1.4.3
# https://leetcode.com/problems/three-divisors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isThree(self, n: int) -> bool:
        return sum(n % i == 0 for i in range(1, n+1)) == 3
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isThree(n)
    print("\noutput:", serialize(ans, "boolean"))
