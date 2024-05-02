# Created by asetti2002 at 2024/05/01 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minOperations(self, n: int) -> int:
        return bin(n)[2:].count('1') + len(bin(n)) - 3
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minOperations(n)
    print("\noutput:", serialize(ans, "integer"))
