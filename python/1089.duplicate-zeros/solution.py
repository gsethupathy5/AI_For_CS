# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/duplicate-zeros/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    duplicateZeros(arr)
    ans = arr
    print("\noutput:", serialize(ans, "List[int]"))