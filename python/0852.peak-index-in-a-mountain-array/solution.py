# Created by asetti2002 at 2024/04/25 19:30
# leetgo: 1.4.3
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().peakIndexInMountainArray(arr)
    print("\noutput:", serialize(ans, "integer"))
