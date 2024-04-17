# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/cracking-the-safe/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().crackSafe(n, k)
    print("\noutput:", serialize(ans, "string"))
