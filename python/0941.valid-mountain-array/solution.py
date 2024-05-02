# Created by asetti2002 at 2024/04/25 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        if i == 0 or i == len(arr) - 1:
            return False
        
        while i < len(arr) - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        return i == len(arr) - 1
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validMountainArray(arr)
    print("\noutput:", serialize(ans, "boolean"))
