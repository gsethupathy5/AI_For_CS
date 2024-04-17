# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/bulb-switcher-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    presses: int = deserialize("int", read_line())
    ans = Solution().flipLights(n, presses)
    print("\noutput:", serialize(ans, "integer"))
