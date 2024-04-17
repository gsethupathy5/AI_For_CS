# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimizeTheDifference(mat, target)
    print("\noutput:", serialize(ans, "integer"))
