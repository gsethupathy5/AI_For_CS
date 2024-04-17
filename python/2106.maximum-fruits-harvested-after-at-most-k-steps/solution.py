# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    fruits: List[List[int]] = deserialize("List[List[int]]", read_line())
    startPos: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxTotalFruits(fruits, startPos, k)
    print("\noutput:", serialize(ans, "integer"))
