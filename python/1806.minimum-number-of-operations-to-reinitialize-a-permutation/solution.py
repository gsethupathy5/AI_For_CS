# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().reinitializePermutation(n)
    print("\noutput:", serialize(ans, "integer"))
