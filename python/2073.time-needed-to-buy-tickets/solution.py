# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/time-needed-to-buy-tickets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tickets: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().timeRequiredToBuy(tickets, k)
    print("\noutput:", serialize(ans, "integer"))
