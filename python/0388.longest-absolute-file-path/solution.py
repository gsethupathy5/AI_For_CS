# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-absolute-file-path/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    input: str = deserialize("str", read_line())
    ans = Solution().lengthLongestPath(input)
    print("\noutput:", serialize(ans, "integer"))
