# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/k-inverse-pairs-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kInversePairs(n, k)
    print("\noutput:", serialize(ans, "integer"))