# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/coin-change-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    amount: int = deserialize("int", read_line())
    coins: List[int] = deserialize("List[int]", read_line())
    ans = Solution().change(amount, coins)
    print("\noutput:", serialize(ans, "integer"))
