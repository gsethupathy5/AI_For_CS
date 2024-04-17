# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/check-array-formation-through-concatenation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    pieces: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFormArray(arr, pieces)
    print("\noutput:", serialize(ans, "boolean"))
