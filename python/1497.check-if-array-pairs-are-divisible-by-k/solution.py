# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().canArrange(arr, k)
    print("\noutput:", serialize(ans, "boolean"))
