# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().containsPattern(arr, m, k)
    print("\noutput:", serialize(ans, "boolean"))
