# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/reach-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reachNumber(self, target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    ans = Solution().reachNumber(target)
    print("\noutput:", serialize(ans, "integer"))
