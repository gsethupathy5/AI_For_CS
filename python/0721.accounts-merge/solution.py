# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/accounts-merge/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    accounts: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().accountsMerge(accounts)
    print("\noutput:", serialize(ans, "string[][]"))