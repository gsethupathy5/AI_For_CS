# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/richest-customer-wealth/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    accounts: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumWealth(accounts)
    print("\noutput:", serialize(ans, "integer"))
