# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/adding-two-negabinary-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().addNegabinary(arr1, arr2)
    print("\noutput:", serialize(ans, "integer[]"))
