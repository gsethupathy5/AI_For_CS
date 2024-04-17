# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-money-to-maximum-children/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    money: int = deserialize("int", read_line())
    children: int = deserialize("int", read_line())
    ans = Solution().distMoney(money, children)
    print("\noutput:", serialize(ans, "integer"))
