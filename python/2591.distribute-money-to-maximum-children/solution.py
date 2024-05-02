# Created by asetti2002 at 2024/05/01 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-money-to-maximum-children/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children or money > 4 * children:
            return -1
        elif money % 8 == 0 or money % 8 == 1:
            return 1
        elif money % 8 == 2 or money % 8 == 3:
            return 2
        else:
            return money // 8
# @lc code=end

if __name__ == "__main__":
    money: int = deserialize("int", read_line())
    children: int = deserialize("int", read_line())
    ans = Solution().distMoney(money, children)
    print("\noutput:", serialize(ans, "integer"))
