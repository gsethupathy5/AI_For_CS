# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(amount) + sum(amount) - 1
# @lc code=end

if __name__ == "__main__":
    amount: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fillCups(amount)
    print("\noutput:", serialize(ans, "integer"))
