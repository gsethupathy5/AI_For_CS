# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    flowers: List[int] = deserialize("List[int]", read_line())
    newFlowers: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    full: int = deserialize("int", read_line())
    partial: int = deserialize("int", read_line())
    ans = Solution().maximumBeauty(flowers, newFlowers, target, full, partial)
    print("\noutput:", serialize(ans, "long"))
