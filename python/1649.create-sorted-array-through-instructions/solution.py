# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/create-sorted-array-through-instructions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    instructions: List[int] = deserialize("List[int]", read_line())
    ans = Solution().createSortedArray(instructions)
    print("\noutput:", serialize(ans, "integer"))
