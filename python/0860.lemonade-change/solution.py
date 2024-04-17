# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/lemonade-change/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    bills: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lemonadeChange(bills)
    print("\noutput:", serialize(ans, "boolean"))
