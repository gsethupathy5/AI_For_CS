# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    packages: List[int] = deserialize("List[int]", read_line())
    boxes: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minWastedSpace(packages, boxes)
    print("\noutput:", serialize(ans, "integer"))
