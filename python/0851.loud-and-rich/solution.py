# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/loud-and-rich/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    richer: List[List[int]] = deserialize("List[List[int]]", read_line())
    quiet: List[int] = deserialize("List[int]", read_line())
    ans = Solution().loudAndRich(richer, quiet)
    print("\noutput:", serialize(ans, "integer[]"))
