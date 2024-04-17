# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().findTheDistanceValue(arr1, arr2, d)
    print("\noutput:", serialize(ans, "integer"))
