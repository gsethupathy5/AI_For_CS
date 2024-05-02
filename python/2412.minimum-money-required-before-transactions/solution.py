# Created by asetti2002 at 2024/05/01 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-money-required-before-transactions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_cost = sum(transaction[0] for transaction in transactions)
        return total_cost
# @lc code=end

if __name__ == "__main__":
    transactions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumMoney(transactions)
    print("\noutput:", serialize(ans, "long"))
