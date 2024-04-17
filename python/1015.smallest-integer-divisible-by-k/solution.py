# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-integer-divisible-by-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRepunitDivByK(k)
    print("\noutput:", serialize(ans, "integer"))
