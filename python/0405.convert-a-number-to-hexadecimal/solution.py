# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def toHex(self, num: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().toHex(num)
    print("\noutput:", serialize(ans, "string"))
