# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-values-from-labels/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    labels: List[int] = deserialize("List[int]", read_line())
    numWanted: int = deserialize("int", read_line())
    useLimit: int = deserialize("int", read_line())
    ans = Solution().largestValsFromLabels(values, labels, numWanted, useLimit)
    print("\noutput:", serialize(ans, "integer"))
