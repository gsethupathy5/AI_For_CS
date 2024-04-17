# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/least-operators-to-express-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().leastOpsExpressTarget(x, target)
    print("\noutput:", serialize(ans, "integer"))
