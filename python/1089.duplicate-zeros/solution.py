# Created by asetti2002 at 2024/04/25 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/duplicate-zeros/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    duplicateZeros(arr)
    ans = arr
    print("\noutput:", serialize(ans, "List[int]"))
