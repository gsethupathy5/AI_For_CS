# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-binary-string-after-change/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    binary: str = deserialize("str", read_line())
    ans = Solution().maximumBinaryString(binary)
    print("\noutput:", serialize(ans, "string"))
