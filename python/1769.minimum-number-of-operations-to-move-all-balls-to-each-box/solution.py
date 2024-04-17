# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    boxes: str = deserialize("str", read_line())
    ans = Solution().minOperations(boxes)
    print("\noutput:", serialize(ans, "integer[]"))
