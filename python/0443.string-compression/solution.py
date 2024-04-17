# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/string-compression/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def compress(self, chars: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    chars: List[str] = deserialize("List[str]", read_line())
    ans = Solution().compress(chars)
    print("\noutput:", serialize(ans, "integer"))
