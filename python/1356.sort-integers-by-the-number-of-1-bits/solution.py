# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortByBits(arr)
    print("\noutput:", serialize(ans, "integer[]"))
