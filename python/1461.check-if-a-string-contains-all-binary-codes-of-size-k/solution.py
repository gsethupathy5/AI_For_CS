# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().hasAllCodes(s, k)
    print("\noutput:", serialize(ans, "boolean"))
