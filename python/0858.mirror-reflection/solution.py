# Created by asetti2002 at 2024/04/25 19:31
# leetgo: 1.4.3
# https://leetcode.com/problems/mirror-reflection/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while q % p != 0:
            p, q = q, p % q
        return 1 if (p // q) % 2 == 0 else 0 if (q // p) % 2 == 0 else 2
# @lc code=end

if __name__ == "__main__":
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().mirrorReflection(p, q)
    print("\noutput:", serialize(ans, "integer"))
