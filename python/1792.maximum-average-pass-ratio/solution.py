# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-average-pass-ratio/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        

# @lc code=end

if __name__ == "__main__":
    classes: List[List[int]] = deserialize("List[List[int]]", read_line())
    extraStudents: int = deserialize("int", read_line())
    ans = Solution().maxAverageRatio(classes, extraStudents)
    print("\noutput:", serialize(ans, "double"))
