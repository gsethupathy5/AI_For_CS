# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/best-poker-hand/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    ranks: List[int] = deserialize("List[int]", read_line())
    suits: List[str] = deserialize("List[str]", read_line())
    ans = Solution().bestHand(ranks, suits)
    print("\noutput:", serialize(ans, "string"))
