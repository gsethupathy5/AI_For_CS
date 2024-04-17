# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minStoneSum(piles, k)
    print("\noutput:", serialize(ans, "integer"))
