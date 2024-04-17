# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    boxes: List[List[int]] = deserialize("List[List[int]]", read_line())
    portsCount: int = deserialize("int", read_line())
    maxBoxes: int = deserialize("int", read_line())
    maxWeight: int = deserialize("int", read_line())
    ans = Solution().boxDelivering(boxes, portsCount, maxBoxes, maxWeight)
    print("\noutput:", serialize(ans, "integer"))
