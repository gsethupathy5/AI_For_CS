# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/2-keys-keyboard/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSteps(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minSteps(n)
    print("\noutput:", serialize(ans, "integer"))
