# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/string-compression-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getLengthOfOptimalCompression(s, k)
    print("\noutput:", serialize(ans, "integer"))
