# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    blocks: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumRecolors(blocks, k)
    print("\noutput:", serialize(ans, "integer"))
