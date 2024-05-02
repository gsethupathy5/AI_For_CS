# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        count = 0
        
        for i in range(n - k + 1):
            if blocks[i:i+k].count('B') < k:
                count += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    blocks: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumRecolors(blocks, k)
    print("\noutput:", serialize(ans, "integer"))
