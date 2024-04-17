# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-common-subpath/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    paths: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().longestCommonSubpath(n, paths)
    print("\noutput:", serialize(ans, "integer"))
