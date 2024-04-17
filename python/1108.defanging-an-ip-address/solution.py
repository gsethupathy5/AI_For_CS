# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/defanging-an-ip-address/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def defangIPaddr(self, address: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    address: str = deserialize("str", read_line())
    ans = Solution().defangIPaddr(address)
    print("\noutput:", serialize(ans, "string"))
