# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/invalid-transactions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    transactions: List[str] = deserialize("List[str]", read_line())
    ans = Solution().invalidTransactions(transactions)
    print("\noutput:", serialize(ans, "string[]"))
