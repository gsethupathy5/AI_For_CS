# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/cut-off-trees-for-golf-event/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    forest: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cutOffTree(forest)
    print("\noutput:", serialize(ans, "integer"))
