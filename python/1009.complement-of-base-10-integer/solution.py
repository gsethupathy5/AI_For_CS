# Created by asetti2002 at 2024/04/25 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/complement-of-base-10-integer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join(['1' if x == '0' else '0' for x in bin(n)[2:]]), 2)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().bitwiseComplement(n)
    print("\noutput:", serialize(ans, "integer"))
