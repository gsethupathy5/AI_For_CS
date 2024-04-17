# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/validate-ip-address/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    queryIP: str = deserialize("str", read_line())
    ans = Solution().validIPAddress(queryIP)
    print("\noutput:", serialize(ans, "string"))
