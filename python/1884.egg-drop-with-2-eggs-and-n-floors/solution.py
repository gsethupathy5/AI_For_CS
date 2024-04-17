# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoEggDrop(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().twoEggDrop(n)
    print("\noutput:", serialize(ans, "integer"))
