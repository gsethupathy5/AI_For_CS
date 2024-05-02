# Created by asetti2002 at 2024/04/25 20:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mctFromLeafValues(arr)
    print("\noutput:", serialize(ans, "integer"))
