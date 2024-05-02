# Created by asetti2002 at 2024/05/01 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/best-poker-hand/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits_set = set(suits)
        ranks_set = set(ranks)
        
        if len(suits_set) == 1:
            return "Flush"
        elif any(ranks.count(rank) >= 3 for rank in ranks_set):
            return "Three of a Kind"
        elif any(ranks.count(rank) == 2 for rank in ranks_set):
            return "Pair"
        else:
            return "High Card"
# @lc code=end

if __name__ == "__main__":
    ranks: List[int] = deserialize("List[int]", read_line())
    suits: List[str] = deserialize("List[str]", read_line())
    ans = Solution().bestHand(ranks, suits)
    print("\noutput:", serialize(ans, "string"))
