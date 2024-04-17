# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    adjacentPairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().restoreArray(adjacentPairs)
    print("\noutput:", serialize(ans, "integer[]"))
