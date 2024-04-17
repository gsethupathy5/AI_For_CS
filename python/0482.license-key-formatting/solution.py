# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/license-key-formatting/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().licenseKeyFormatting(s, k)
    print("\noutput:", serialize(ans, "string"))
