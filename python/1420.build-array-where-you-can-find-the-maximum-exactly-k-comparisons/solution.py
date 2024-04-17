# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numOfArrays(n, m, k)
    print("\noutput:", serialize(ans, "integer"))
