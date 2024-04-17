# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-units-on-a-truck/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    boxTypes: List[List[int]] = deserialize("List[List[int]]", read_line())
    truckSize: int = deserialize("int", read_line())
    ans = Solution().maximumUnits(boxTypes, truckSize)
    print("\noutput:", serialize(ans, "integer"))
