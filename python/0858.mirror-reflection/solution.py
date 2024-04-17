# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/mirror-reflection/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().mirrorReflection(p, q)
    print("\noutput:", serialize(ans, "integer"))
