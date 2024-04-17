# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findRotation(mat, target)
    print("\noutput:", serialize(ans, "boolean"))
